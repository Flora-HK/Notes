# Typing操作

在 Python 中，**类型注解（type hints）** 是一种增强代码可读性、便于静态检查的语法，不会影响运行时行为。下面从常见类型和添加方式两方面来说明。

---

### 一、常见类型注解 

1. 一般定义类注解



1. 生成器函数注解
1. 覆写父类方法，需要声明@override

---

### 二、类型注解实例

直接在变量名后加 `: 类型`。可以在赋值时同时注解，也可以单独注解。

```python
name: str = "Alice"
age: int                      # 只注解，未初始化
from typing import Optional
nickname: Optional[str] = None
```

对参数和返回值分别注解，返回值用 `->` 指示。

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

from typing import Union
def get_id(value: Union[int, str]) -> str:
    return str(value)
```

- 实例属性：通常在 `__init__` 中对 `self.attr` 加注解。
- 类属性：使用 `ClassVar` 表明该变量属于类而非实例。

```python
from typing import ClassVar

class Counter:
    total: ClassVar[int] = 0

    def __init__(self) -> None:
        self.value: int = 0   # 实例属性注解
```

当类型尚未定义时，可以用**字符串形式**的注解，或使用 `from __future__ import annotations`（Python 3.10+ 推荐）。

```python
from __future__ import annotations

class Node:
    def __init__(self, value: int, left: Node | None = None):
        self.left = left
```

旧写法：`left: 'Node' = None`。

```python
from typing import TypeVar, Generic

T = TypeVar('T') #此处的T实际为一个占位符，等到实际使用的时候才确定他的类型和内容

def first_item(items: list[T]) -> T:
    return items[0]
 # 以上为泛型函数，表示输入列表为某个T类型的列表，输出也为某个T类型，当进行输入时，类型检查器会检查：
 # 1，输入的list内容是不是统一的某个T类型（可能都为str，也可能都为int，但不能是int + str）
 # 2. 得出T类型具体是哪种类型，并输出对应的某个类型的内容
 # 因此，如果你调用 first_item([1, 2, 3])，检查器推断出 T = int，所以函数返回 int；若调用 first_item(["a", "b"])，T = str，返回 str。如果你尝试 first_item([1, "a"])，检查器会报警告，因为列表元素类型不统一。
class Stack(Generic[T]): 
# 定义了一个‘泛型类’，即该class里面可以存储T类型的变量，如果定义为 Stack[int]()，则可以存储int类；定义为Stack[str]()，则可以存储str类。T就是一个延迟解释类，具体T类是什么类，在运行时根据环境决定
    def push(self, item: T) -> None: ...
    def pop(self) -> T: ...
    # 在class下开发中，T类可以当做一般类直接使用
```

```python
from typing import TypedDict

class Movie(TypedDict):
    title: str
    year: int

movie: Movie = {"title": "Inception", "year": 2010}
```

```python
from typing import Protocol

class Flyer(Protocol):
# Protocol更像是让Flyer变成一个协议，后续如果其他变量后面带上Flyer，则证明该处的变量需要是满足Flyer协议的变量，也就是它应该是一个'Flyer类'
    def fly(self) -> None: ...

def take_off(obj: Flyer) -> None:
# ‘obj: Flyer’表示obj必须是一个满足Flyer协议的变量，要属于Flyer类
    obj.fly()
```

任何实现了 `fly` 方法的对象都可以传入，无需显式继承。

```python
from typing import Any, Callable, ParamSpec, TypeVar
from functools import wraps
import time

# 1. 日志装饰器
P = ParamSpec('P')
R = TypeVar('R')

def log(fn: Callable[P, R]) -> Callable[P, R]: #表示log装饰器接收任意签名的可调用对象，并返回一个可调用对象
    '''简单的日志装饰器'''
    @wraps(fn)
    def inner(*args: P.args, **kwargs: P.kwargs) -> R: 
        print(f'{'='*30}装饰器1作用开始{'='*30}')
        print(f'[LOG]函数{fn.__name__}即将被调用')
        # 下面这样的try方法结构更加健壮
        try:
            res = fn(*args, **kwargs)
            print(f'[LOG]函数{fn.__name__}调用完毕，返回值为{res}')
            print(f'{'='*30}装饰器1作用结束{'='*30}')
            return res
        except Exception as e:
            print(f'[LOG]函数调用失败，抛出异常：{e!r}')
            print(f'{'='*30}装饰器1作用结束{'='*300}')
            raise
    return inner
```

1. 其中 `ParamSpec` 实际上代表着“**一整组参数**”的变量，其有两个常用属性来代指变量类：

（有 `P = ParamSpec('P')`的前提）

1. `P.args` ：代表所有“位置参数“的元组类型
1. `P.kwargs` ：代表所有”关键字参数”的字典类型



1. 其中的 `TypeVar` 代表**单个类型**的变量，代码中常见 `T = TypeVar('T')` 是代表设定了一个T的未知类型变量。



