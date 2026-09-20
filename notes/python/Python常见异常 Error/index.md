# Python常见异常 Error

### 一、内置异常层级

```python
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 ├── GeneratorExit
 └── Exception                    ← 大部分异常继承自此
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    └── OverflowError
      ├── AttributeError
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── NameError
      ├── OSError
      │    ├── FileNotFoundError
      │    ├── PermissionError
      │    └── TimeoutError
      ├── TypeError
      ├── ValueError
      ├── StopIteration
      ├── RuntimeError
      └── AssertionError
```

### 二、常见异常速查表

### 三、try 捕获的四种经典写法

```python
# 1. 基础捕获 — 指定异常类型
try:
    num = int(input("输入数字: "))
    result = 100 / num
except ValueError:
    print("输入的不是数字！")
except ZeroDivisionError:
    print("不能除以零！")

# 2. 捕获多个异常，统一处理
try:
    d = {"a": 1}
    print(d["b"])
except (KeyError, IndexError, AttributeError):
    print("数据访问出错了")

# 3. 获取异常对象 — 打印详细信息
try:
    result = 1 / 0
except ZeroDivisionError as e:
    print(f"异常类型: {type(e).__name__}")
    print(f"异常信息: {e}")

# 4. else / finally 完整结构
try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("文件不存在，请检查路径")
else:
    print(f"读取成功，内容长度: {len(content)}")  # 无异常才执行
finally:
    f.close()  # 无论如何都执行，适合释放资源
    print("文件已关闭")
```

### 四、实战中最重要的三条规则

**规则 1：永远捕获具体异常，不要裸 ****`except:`**

```python
# ❌ 坏 — 连 Ctrl+C 都会吞掉
try:
    do_something()
except:
    pass

# ✅ 好 — 精确捕获
try:
    do_something()
except (ConnectionError, TimeoutError) as e:
    logger.error(f"网络错误: {e}")
```

**规则 2：****`finally`**** 用于释放资源，****`else`**** 用于「无异常才执行」**

```python
# finally 典型场景：数据库连接必须关闭
db = None
try:
    db = Database()
    db.execute(sql)
except DatabaseError as e:
    print(f"数据库错误: {e}")
else:
    print("SQL 执行成功")
finally:
    if db:
        db.close()  # 有异常没异常都会关
```

**规则 3：用 ****`raise`**** 保留原始异常链**

```python
# ❌ 坏 — 丢失原始异常信息
try:
    result = process_data(raw)
except ValueError:
    raise RuntimeError("处理失败")

# ✅ 好 — raise from 保留完整调用链
try:
    result = process_data(raw)
except ValueError as e:
    raise RuntimeError("处理数据失败") from e
```

### 五、结合你学习计划的场景

结合你计划中的两个实战场景：

```python
# 场景1：通讯录输入校验（Week 1 Day 3）
class ContactError(Exception):
    """自定义异常 — 通讯录相关错误"""
    pass

def add_contact(name: str, phone: str) -> None:
    if not name.strip():
        raise ContactError("姓名不能为空")
    if not phone.isdigit() or len(phone) != 11:
        raise ContactError("手机号必须为 11 位数字")

# 使用时
try:
    add_contact("", "123")  # 故意传空姓名
except ContactError as e:
    print(f"添加失败: {e}")


# 场景2：API 调用重试装饰器（Week 1 Day 1）
import requests
import time

def retry(times=3):
    """失败自动重试的装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except (requests.ConnectionError,
                        requests.Timeout) as e:
                    if attempt == times:
                        raise  # 最后一次仍失败则抛出
                    print(f"第 {attempt} 次失败，{2}s 后重试...")
                    time.sleep(2)
        return wrapper
    return decorator

@retry(3)
def fetch_weather(city: str):
    resp = requests.get(f"<https://api.weather.com/{city}>", timeout=5)
    resp.raise_for_status()
    return resp.json()
```

### 六、一句话记忆口诀

```plain text
Type错类型，Value错值，Name未定义，Index越了界
Key键不在，Attribute无属性，File找不到，Import没安装
Zero除以零，Assert断言假，Stop迭代尽，Timeout是超时
```

