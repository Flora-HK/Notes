# 函数常见内置属性

Python 函数对象的常见内置属性如下：

## **身份与文档类**

`__doc__`是写在函数定义里第一行的字符串内容

## **参数与签名类**

## **闭包与上下文类**

## 实例演示：

```python
def greet(name: str, greeting: str = "Hello") -> str:
"""向某人打招呼"""
return f"{greeting}, {name}!"
```

```python
print(greet.**name**)        # greet
print(greet.**doc**)         # 向某人打招呼
print(greet.**module**)      # **main**
print(greet.**defaults**)    # ('Hello',)
print(greet.**annotations**) # {'name': <class 'str'>, 'return': <class 'str'>}
print(greet.**code**.co_varnames)  # ('name', 'greeting')
print(greet.**code**.co_argcount)  # 2
```



