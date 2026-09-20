#!/usr/bin/env python3
"""同步多个 Notion 根页面（每个对应一个顶层目录）。"""
import os
import re
import sys
from pathlib import Path
from notion_client import Client

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
PAGE_SPEC = os.environ["NOTION_PAGE_IDS"]
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "notes")

notion = Client(auth=NOTION_TOKEN)
PAGE_SIZE = 100


def clean_filename(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '_', name)
    name = re.sub(r'\s+', ' ', name).strip().rstrip('.')
    return name[:80] or "untitled"


def parse_pages(spec: str):
    """解析 'alias1:id1,alias2:id2,id3' 这种格式。"""
    pages = []
    for item in spec.split(","):
        item = item.strip()
        if not item:
            continue
        if ":" in item:
            alias, pid = item.split(":", 1)
            pages.append((alias.strip(), pid.strip()))
        else:
            pages.append((None, item))
    return pages


def get_title(page: dict) -> str:
    for prop in page.get("properties", {}).values():
        if prop.get("type") == "title":
            return "".join(rt.get("plain_text", "") for rt in prop.get("title", []))
    return "untitled"


def iter_children(block_id: str):
    cursor = None
    while True:
        params = {"page_size": PAGE_SIZE}
        if cursor:
            params["start_cursor"] = cursor
        resp = notion.blocks.children.list(block_id=block_id, **params)
        yield from resp["results"]
        if not resp.get("has_more"):
            return
        cursor = resp["next_cursor"]


def rich_text_to_md(rich_text: list) -> str:
    out = []
    for rt in rich_text:
        text = rt.get("plain_text", "")
        ann = rt.get("annotations", {}) or {}
        href = rt.get("href")
        if ann.get("code"):    text = f"`{text}`"
        if ann.get("bold"):    text = f"**{text}**"
        if ann.get("italic"):  text = f"*{text}*"
        if ann.get("strikethrough"): text = f"~~{text}~~"
        if href:               text = f"[{text}]({href})"
        out.append(text)
    return "".join(out)


def block_to_md(block: dict) -> str:
    btype = block.get("type")
    data = block.get(btype, {})

    if btype == "paragraph":   return rich_text_to_md(data.get("rich_text", [])) + "\n\n"
    if btype == "heading_1":   return f"# {rich_text_to_md(data.get('rich_text', []))}\n\n"
    if btype == "heading_2":   return f"## {rich_text_to_md(data.get('rich_text', []))}\n\n"
    if btype == "heading_3":   return f"### {rich_text_to_md(data.get('rich_text', []))}\n\n"
    if btype == "bulleted_list_item": return f"- {rich_text_to_md(data.get('rich_text', []))}\n"
    if btype == "numbered_list_item": return f"1. {rich_text_to_md(data.get('rich_text', []))}\n"
    if btype == "to_do":
        checked = "x" if data.get("checked") else " "
        return f"- [{checked}] {rich_text_to_md(data.get('rich_text', []))}\n"
    if btype == "code":
        lang = data.get("language", "")
        return f"```{lang}\n{rich_text_to_md(data.get('rich_text', []))}\n```\n\n"
    if btype == "quote":       return f"> {rich_text_to_md(data.get('rich_text', []))}\n\n"
    if btype == "callout":
        emoji = data.get("icon", {}).get("emoji", "💡")
        return f"> {emoji} {rich_text_to_md(data.get('rich_text', []))}\n\n"
    if btype == "divider":     return "---\n\n"
    if btype == "image":
        url = (data.get("file") or data.get("external") or {}).get("url", "")
        cap = rich_text_to_md(data.get("caption", []))
        return f"![{cap}]({url})\n\n"
    if btype == "bookmark":
        url = data.get("url", "")
        cap = rich_text_to_md(data.get("caption", [])) or url
        return f"[{cap}]({url})\n\n"
    return ""


def render_page(page_id: str) -> str:
    pieces, list_buf = [], []
    def flush_list():
        if list_buf:
            pieces.append("".join(list_buf) + "\n")
            list_buf.clear()
    for block in iter_children(page_id):
        if block.get("type") in ("bulleted_list_item", "numbered_list_item"):
            list_buf.append(block_to_md(block))
        else:
            flush_list()
            pieces.append(block_to_md(block))
    flush_list()
    return "".join(pieces)


def walk(page_id: str, out_dir: Path, alias: str | None = None):
    page = notion.pages.retrieve(page_id=page_id)
    title = alias or clean_filename(get_title(page))
    current = out_dir / title
    current.mkdir(parents=True, exist_ok=True)
    print(f"[Page] {current}")

    (current / "index.md").write_text(
        f"# {get_title(page)}\n\n{render_page(page_id)}", encoding="utf-8"
    )

    for child in iter_children(page_id):
        if child.get("type") == "child_page":
            walk(child["id"], current)


def main():
    pages = parse_pages(PAGE_SPEC)
    if not pages:
        print("NOTION_PAGE_IDS 为空", file=sys.stderr); sys.exit(1)

    out = Path(OUTPUT_DIR)
    if out.exists():
        for p in sorted(out.rglob("*"), reverse=True):
            if p.is_file():   p.unlink()
            elif p.is_dir():  p.rmdir()
    out.mkdir(parents=True, exist_ok=True)

    print(f"开始同步 {len(pages)} 个根页面 -> {OUTPUT_DIR}/")
    for alias, pid in pages:
        print(f"-- {alias or '(使用页面原标题)'}: {pid}")
        walk(pid, out, alias)
    print("全部同步完成。")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"失败: {e}", file=sys.stderr); sys.exit(1)
