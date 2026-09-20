# Function Calling

## 一、 TOOLS_SCHEMA：

给LLM的一份工具说明书

一份依据Open AI的TOOLS_SCHEMA示例：

```python
TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询指定城市的当前天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名，例如 '北京'、'上海'",
                    }
                },
                "required": ["city"],
            },
        },
    }
]
```

一个 `schema` 对应一个工具的说明

其中 `properties` 为工具参数说明书， `type` 参数类型、 `description` 参数描述。

`required` 为必填参数清单，通常是一些没有默认值的参数

## 二、 调用完后message的信息追加也有变化：

```python
        # ④ 把 assistant 消息追加（必须含 tool_calls 字段）
        messages.append({
            "role": "assistant",
            "content": msg.content,
            "tool_calls": [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments,
                    },
                }
                for tc in msg.tool_calls
            ],
        })
```

## 三、 终止Loop循环：

```python
 if not msg.tool_calls:
            print(f"\n[第 {turn} 轮] ✅ 模型给出最终回答（不再要求调工具）")
            # 把最终 assistant 消息也回填进 messages，方便最后打印完整历史
            messages.append({"role": "assistant", "content": msg.content})
            break
```

通过检测chat（）函数返回msg的tool_calls来判断LLM是否还需要调用工具

## 四、 循环执行所需调用工具：

```python
        # 逐个执行工具，结果以 role=tool 追加
        for tc in msg.tool_calls:
            name = tc.function.name
            args = json.loads(tc.function.arguments)
            print(f"  → 执行工具: {name}({args})")
            if name == "get_weather":
                result = get_weather(**args)
            else:
                result = f"未知工具: {name}"
            print(f"    = {result}")
            # 关键：tool_call_id 必须和上一条 assistant.tool_calls[*].id 对得上
            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": result,
            })
        # ⑤ 进入下一轮
```

其中函数

```plain text
json.loads()
```

用于将以json形式返回的字符串

```plain text
'{'city':'北京'}'
```

转换成字典

```plain text
{'city':'北京'}
```



