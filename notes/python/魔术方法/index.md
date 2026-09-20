# 魔术方法

**魔术方法（Magic Methods / Dunder Methods）**，特点就是：**在类里实现特定名称的 ****`__xxx__`**** 方法，就能让这个类支持对应的语言特性**。这正是"万物皆对象"的体现。

有以下常用的魔术方法：

---

## 一、对象生命周期

---

## 二、运算符重载

```python
class Vector:
    def __init__(self, x, y):     #  初始化
        self.x, self.y = x, y

    def __add__(self, other):    # 加法： v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):    # 减法： v1 - v2
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, n):        # 乘法： v1 * 3
        return Vector(self.x * n, self.y * n)

    def __eq__(self, other):     # 相等比较： v1 == v2
        return self.x == other.x and self.y == other.y

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2    # 调用 __add__

# 完整运算符方法：
# __neg__(-obj)  __lt__(<)  __le__(<=)  __gt__(>)  __ge__(>=)
# __ne__(!=)  __truediv__(/)  __floordiv__(//)  __mod__(%)
```

---

## 三、像容器一样使用（最常用）

```python
class MyList:
    def __init__(self):
        self.data = []

    def __len__(self):           # len(obj)
        return len(self.data)

    def __getitem__(self, i):    # obj[0]
        return self.data[i]

    def __setitem__(self, i, v): # obj[0] = v
        self.data[i] = v

    def __delitem__(self, i):    # del obj[0]
        del self.data[i]

    def __contains__(self, v):   # v in obj
        return v in self.data

    def __iter__(self):          # for x in obj
        return iter(self.data)

    def __reversed__(self):      # reversed(obj)
        return reversed(self.data)
```

---

## 四、字符串表示

```python
class Person:
    def __str__(self):           # str(obj), print(obj) → 给用户看
        return f'Person({self.name})'

    def __repr__(self):          # repr(obj), 交互环境直接输入变量名 → 给开发者看
        return f"Person('{self.name}', {self.age})"
```

---

## 五、属性访问控制

分别控制了属性的读写删，读（ `__getattr__`）、写（ `__setattr__`）、删（ `__delattr__`）

```python
class Proxy:
    def __getattr__(self, name):       # 访问不存在的属性时，读不存在的属性触发
        return f'属性{name}不存在'

    def __setattr__(self, name, val):  # obj.x = val 时，赋值就触发
        super().__setattr__(name, val)

    def __delattr__(self, name):       # del obj.x 时，删除某属性触发
        super().__delattr__(name)

    def __getattribute__(self, name):  # 每次访问属性都触发（慎用）
        return super().__getattribute__(name)
```

当我们写 `obj.x` 来查询某个对象的值时，有如下访问逻辑线路：

```python
obj.x
↓
调用 **getattribute**('x') ← 一定会被调用
↓
在 **dict** 和类/父类中查找 'x'
↓
找到了 → 直接返回
没找到 → 调用 **getattr**('x') ← 兜底
```

```plain text
[obj.name] = value          访问 [obj.name]           del [obj.name]
│                         │                      │
▼                         ▼                      ▼
setattr('name',           getattribute('name')    delattr('name')
value)                   │                      │
│                         ▼                      super().delattr
▼                    查找属性是否存在                │
super().setattr           │                 从 dict 移除
('name', value)         ┌────┴────┐
▼                      ▼         ▼
                      找到了      没找到
                      │         │
                      ▼         ▼
                      返回属性值  getattr('name')
                                  │
                                  └── 你自定义的兜底逻辑
```

一句话总结：**getattribute** 拦全部，**getattr** 兜底不存在的，**setattr** 拦赋值，**delattr** 拦删除。内部操作必用 super() 避免无限递归。

---

## 六、可调用对象与函数式

```python
class Multiplier:
    def __call__(self, x):       # 让实例像函数一样被调用
        return x * 2

double = Multiplier()
double(5)  # → 10，对象() 触发 __call__

class LazySeq:
    def __len__(self): ...
    def __getitem__(self, i): ...
    # 实现以上两个方法后，可直接用 iter()、for、in 等
```

---

## 七、上下文管理器（with块的打开和关闭）

```python
class Managed:
    def __enter__(self): return self    # with 进入
    def __exit__(self, *args): ...      # with 退出
```

也可以使用 `@contextmanager` 来简化包装过程：

# 类写法 — 10 行

```python
class Timer:
    def **enter**(self):
        self.start = time.time()
        return self
        
        
    def __exit__(self, *args):
    self.end = time.time()
    print(f'耗时: {self.end - self.start:.3f}s')
    
with Timer():
   time.sleep(1)
```

# @contextmanager 写法 — 5 行

```python
from contextlib import contextmanager
import time
```

```python
@contextmanager
def timer():
    start = time.time()
    yield
    print(f'耗时: \{time.time() - start:.3f\}s')
```

```python
with timer():
    time.sleep(1)
```

---

## 八、描述符（`@property` 的底层）

```python
class Positive:
    def __get__(self, obj, owner):     # 读取属性时
        return obj._val

    def __set__(self, obj, value):     # 赋值时
        if value <= 0:
            raise ValueError('必须是正数')
        obj._val = value
```

---

## 一张图看清关系

```plain text
你用 Python 语法 → Python 自动找对应的 __xxx__ 方法 → 执行你定义的逻辑

len(obj)          →  obj.__len__()
obj[0]            →  obj.__getitem__(0)
obj + other       →  obj.__add__(other)
for x in obj      →  obj.__iter__()
with obj as x     →  obj.__enter__() / obj.__exit__()
obj()             →  obj.__call__()
str(obj)          →  obj.__str__()
x in obj          →  obj.__contains__(x)
```

**核心逻辑就是你说的：在类里定义特定方法 → Python 语言特性自动生效。** 这就是 Python "协议"（Protocol）的思想——不管你是什么类型，只要你实现了 `__iter__`，你就能被 `for` 循环遍历；实现了 `__enter__`/`__exit__`，你就能被 `with` 管理。鸭子类型 + 魔术方法 = Python 的灵活性来源。



