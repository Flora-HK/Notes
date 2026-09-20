# Agent范式

## 一、 React：Thought-Action-Observation循环

即让大模型先输出一个思考（Thought），在给出一个工具调用行为请求（Action），然后根据工具调用结果返回（Observation）给出新的思考（Thought），循环往复进行

prompt包含历史对话每一步的Thought-Action-Observation对，当模型不需要调用时，会在Thought和Action中进行反馈，即停止循环





