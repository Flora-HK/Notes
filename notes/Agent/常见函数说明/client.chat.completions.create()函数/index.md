# client.chat.completions.create()函数

## 一、函数签名

该函数是 **OpenAI Python SDK 的核心方法**，向 LLM API 发起一次对话补全请求

其函数签名如下:

```python
def create(
self,
*,
model: str,                          # 模型名称
messages: list[dict],                 # 对话历史
temperature: float | None = None,     # 随机性 (0~2)
stream: bool = False,                 # 是否流式返回
tools: list[dict] | None = None,      # Function Calling 工具定义
tool_choice: str | dict | None = None,# 工具调用策略
max_tokens: int | None = None,        # 最大输出 token 数
...
) -> ChatCompletion | Stream[ChatCompletionChunk]:
```

## 二、 函数参数

## **`client.chat.completions.create()`**** 参数详解**

### **核心参数一览**

`tool_choice` 有 4 种取值：

99% 场景用 `auto` 就够。

## 三、 函数返回信息

该函数返回变量信息：

```plain text
response  # ChatCompletion 对象
├── response.choices  # 候选回复列表
│   └── response.choices[0]  # ChatCompletionChoice
│       └── response.choices[0].message  # ← 这个才是代码里的 msg
│           ├── .content
│           └── .tool_calls
│               ├── [0].id
│               ├── [0].type
│               └── [0].function
│                   ├── .name
│                   └── .arguments
├── response.usage  # token 用量
├── response.model  # 模型名
└── response.id  # 请求 ID
```

其中的 response.choices[0].message 就是代码示例中的chat()函数返回的msg



