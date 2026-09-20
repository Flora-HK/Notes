# Agent记忆（message）

LLM没有记忆，记忆需要通过message来传入，message初始包含以下两部分：

```python
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": QUESTION},
    ]
```

SYSTEM_PROMPT：我们给大模型的性格/初步设定

```python
SYSTEM_PROMPT = f"""你是一个会用工具的助手。

可用工具：
{tools_description()}

每次需要调工具时，**只输出一行 JSON**，格式：
  {{"tool": "工具名", "args": {{"参数名": "参数值"}}}}

如果你已经能直接回答用户问题（不需要再调工具），输出：
  {{"final": "你的最终回答"}}

不要输出任何 JSON 以外的文字。
"""
```

QUESTION：提供给LLM的问题

```python
QUESTION = "请帮我抓取 [https://example.com](https://example.com/) 的网页内容，告诉我它有多少字节，并把这个字节数除以 7。"
```

最后，要及时将工具调用结果传回上下文message中：

assistant代表上一步的请求工具调用语句；user代表调用工具的结果

```python
        messages.append({"role": "assistant", "content": raw})
        messages.append(
            {"role": "user", "content": f"上一步工具的结果：{obs}\n请继续。"}
        )
```



