# 内省和反射机制



**`inspect.signature`** 是 Python 标准库的**内省/反射**机制。它能**读取函数定义时的签名元信息**，而不需要实际调用函数。

1.  常见用法：

引入inspect模块，在该模块下使用

```python
import inspect

def get_weather(city: str, unit: str = "celsius") -> str:
    """查询天气"""
    ...

sig = inspect.signature(get_weather)
print(sig)  # (city: str, unit: str = 'celsius') -> str

```

1. 核心属性：**`sig.parameters`**

最关键的部分，返回一个**有序字典** `MappingProxyType`，key 是参数名，value 是 `inspect.Parameter` 对象：

例：

```python
sig = inspect.signature(get_weather)

for name, param in sig.parameters.items(): #常用遍历方法
print(f"name={name!r}, param={param!r}")
```

输出：

```python
name='city', param=<Parameter "city: str">
name='unit', param=<Parameter "unit: str = 'celsius'">
```

1. **`Parameter`**** 对象的关键属性**

以 `def foo(x: int, y: str = "hello", *args, **kwargs) -> bool:` 为例：

1. 先用 `for name, param in sig.parameters.items()` 遍历取出单个 `para` 值，再根据不同的属性名可以访问对应的返回值（eg：`param.name`）
1. 常用 `if param.default is inspect.Parameter.empty:` 来检测一个 `Parameter` 对象是否有默认值：



