# Loop循环

```python
def mini_agent() -> None:
    print("\n\n" + "=" * 60)
    print("【实验 ② · 最小 Agent Loop】")
    print("=" * 60)
    print(f"问题: {QUESTION}\n")

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": QUESTION},
    ]

    for turn in range(1, 6):  # 最多 5 轮，防止跑飞
        print(f"--- 第 {turn} 轮 ---")
        resp = llm_chat(
            messages,
            temperature=0,
            client=client,
            model=MODEL,
        )
        raw = resp.content
        print(f"模型输出: {raw}")

        step = parse_step(raw)

        # ① 模型给出最终答案
        if "final" in step:
            print(f"\n🎯 最终答案: {step['final']}")
            return

        # ② 模型要调工具
        tool_name = step["tool"]
        print(f"{tool_name}\n")
        args = step.get("args", {})
        if tool_name not in TOOLS:
            obs = f"未知工具: {tool_name}"
        else:
            func, _ = TOOLS[tool_name]
            obs = func(**args)
        print(f"工具结果: {obs}\n")

        # 把"工具调用"和"工具结果"都拼回 messages，让模型看到下一步
        messages.append({"role": "assistant", "content": raw})
        messages.append(
            {"role": "user", "content": f"上一步工具的结果：{obs}\n请继续。"}
        )

    print("⚠️ 达到最大轮次，仍未给出最终答案。")
```

1. 将循环调用次数进行一定的限制，防止LLM出错进行无限调用
1. 反复检查变量step内容，如果出现“final”字节段的返回，就截止循环，输出大模型内容



