# pydantic类型校验

# pydantic 类型校验

> **环境**：pydantic **2.13.5** / Python 3.14.3 ｜ 全文按 **v2** 语法写

> **配套**：《开源项目学习计划5》W0（精读模板 `core/config.py` = pydantic-settings）、FastAPI 网课 9–13 集（Field / 响应类型）、项目一 `schemas` 与 SQLModel

> **说明**：标注「实测」的结论已在本机 pydantic 2.13.5 上跑过

---

## 一、什么是 pydantic

### 1.1 一句话定位

pydantic 是 **基于类型注解的运行时数据校验 + 序列化库**。

关键在「运行时」三个字：

```python
def f(x: int) -> int:      # 注解只是提示
    return x

f("hello")                 # 完全不报错，照样返回 'hello'
```

### 1.2 它解决什么问题

后端收到的数据永远不可信：HTTP body 是 JSON、查询参数是字符串、配置文件是文本。手写 `if not isinstance(...)` 很快失控。pydantic 把校验规则**声明式写在类型注解里**，一次声明同时得到三样东西：

1. **校验（validation）**：dict / JSON → 模型实例；不合法就报错，且报错带字段路径
1. **序列化（dump）**：模型 → dict / JSON，可排除字段、按别名输出
1. **JSON Schema**：自动生成 —— FastAPI 的 `/docs` 页面就是这么来的

### 1.3 为什么必须学它

- **FastAPI**：请求体、查询参数、响应模型全靠 pydantic，写 FastAPI 不写 pydantic 等于没写
- **SQLModel**：`SQLModel = SQLAlchemy + pydantic`，模板里 `models.py` 每个模型都是 pydantic 模型
- **pydantic-settings**：模板 `core/config.py` 用 `BaseSettings` 读 `.env` 并校验类型
- **生态**：OpenAI Agents SDK、LangChain、LangGraph 的入参出参全是 pydantic 模型（项目二 W3 精读 Agent SDK 会反复遇到）
- **面试**：`FastAPI 怎么做参数校验`、`为什么 pydantic 默认会强转类型` 都是高频追问

### 1.4 v1 → v2 分水岭（必须先记住）

v2 把核心用 Rust 重写（`pydantic-core`），性能大幅提升，同时 **API 大改**。网上大量教程仍是 v1，照抄必踩坑：

> 判断依据：导入里有 `field_validator`、`ConfigDict` 就是 v2。本机 `pydantic.VERSION == '2.13.5'`。

---

## 二、最小可用范式

```python
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True          # 有默认值 → 可以不传

u = User(id="7", name="Tom")        # 注意：字符串 "7" 被自动转成 int 7
print(u)                            # id=7 name='Tom' is_active=True
print(u.model_dump())               # {'id': 7, 'name': 'Tom', 'is_active': True}
print(u.model_dump_json())          # {"id":7,"name":"Tom","is_active":true}

# 从 dict / JSON 入口（接 HTTP 数据的标准姿势）
u2 = User.model_validate({"id": 8, "name": "Jerry"})
u3 = User.model_validate_json('{"id": 9, "name": "Ann"}')

# 校验失败
try:
    User(id="abc", name="x")
except ValidationError as e:
    print(e.error_count())          # 1
    print(e.errors()[0]["loc"])     # ('id',)
    print(e.errors()[0]["type"])    # 'int_parsing'
    print(e.errors()[0]["msg"])     # Input should be a valid integer, unable to parse string as an integer
```

**必会 API 速记**

> ⚠️ 关键心智模型：**pydantic 默认是「宽容模式」（lax）——先尝试转换，转不了才报错**。`"7" → 7`、`1.0 → 1`、`True → 1`（对 `int` 字段）都成立。想要「类型不符就报错」必须显式开 strict（见 4.8）。

---

## 三、约束写在两个地方

**轴 1 · 注解本身的类型** —— 决定「允许什么类型」

`int` / `str` / `list[str]` / `Literal[...]` / `Enum` / `datetime` / `UUID4` / `Decimal` …

**轴 2 · 附加的约束参数** —— 决定「在这个类型上还要满足什么条件」

`Field(gt=0, max_length=10)` / `StringConstraints(...)` / `ConfigDict(...)`

### 两种写法，推荐第二种

```python
from typing import Annotated
from pydantic import BaseModel, Field

# 写法 A：赋值式（最直观）
class P1(BaseModel):
    age: int = Field(gt=0, le=150)

# 写法 B：Annotated 类型式（推荐）
Age  = Annotated[int, Field(gt=0, le=150)]      # 可提取成别名，全局复用
Name = Annotated[str, Field(min_length=1, max_length=32)]

class P2(BaseModel):
    name: Name
    age: Age
    score: Annotated[float, Field(ge=0, le=100)] = 0.0
```

**为什么推荐 ****`Annotated`**：约束与类型绑在一起，可做成**可复用的类型别名**（一个 `Age` 全项目通用）；与 `typing` 生态兼容，mypy 也能读到；且不像写法 A 那样容易把 `Field()` 误读成「有默认值」（`age: int = Field(gt=0)` 其实是**必填**）。

> ⚠️ 反面教材：`Field(strip_whitespace=True)`

> **v2 的 ****`Field`**** 没有这个参数**。实测不会报错，但会静默失效并抛一条 deprecation 警告，字符串里的空格**原封不动**。要裁剪空格得用 `StringConstraints` 或 `ConfigDict(str_strip_whitespace=True)`。

---

## 四、常见类型约束及用法（举例）

### 4.1 数值约束

```python
from typing import Annotated
from pydantic import BaseModel, Field, PositiveInt, StrictInt

class Product(BaseModel):
    qty: PositiveInt                                        # 等价 Annotated[int, Field(gt=0)]
    price: Annotated[float, Field(gt=0, le=1_000_000)]       # 大于 0，不超过 100 万
    discount: Annotated[float, Field(ge=0, lt=1)] = 0.0      # 左闭右开 [0, 1)
    batch: Annotated[int, Field(multiple_of=10)]             # 必须是 10 的整数倍
    strict_id: StrictInt                                     # 拒绝 "1"、1.0、True

p = Product(qty=3, price=9.9, batch=30, strict_id=1)
```

**便捷类型**：`PositiveInt` / `NonNegativeInt` / `NegativeInt` / `NonPositiveInt` / `PositiveFloat` / `NonNegativeFloat` / `NegativeFloat` / `NonPositiveFloat`。

> 🔴 **`bool`**** 是 ****`int`**** 的子类**：`int` 字段传 `True` 会被转成 `1`（实测通过）。要挡住布尔值必须用 `StrictInt` 或 `Field(strict=True)`。

> `Decimal` 的小数位是**报错而非四舍五入** —— 实测 `Field(max_digits=5, decimal_places=2)` 传 `"42.123"` 直接抛 `decimal_max_places`。金额场景正需要这个行为。

> `conint(gt=0)` / `confloat(...)` 在 v2 仍可用，但属遗留写法，新代码统一用 `Annotated[int, Field(gt=0)]`。

### 4.2 字符串约束

v2 里字符串的「变换类」约束（裁剪、大小写）**不在 ****`Field`**** 上**，而在 `StringConstraints`：

```python
from typing import Annotated
from pydantic import BaseModel, Field, StringConstraints

Username = Annotated[
    str,
    StringConstraints(strip_whitespace=True, to_lower=True, min_length=3, max_length=20),
]
Phone = Annotated[str, StringConstraints(pattern=r"^1[3-9]\d{9}$")]

class Signup(BaseModel):
    username: Username
    phone: Phone
    bio: str = Field(default="", max_length=200)     # 只做长度约束时可继续用 Field

Signup(username="  Alice  ", phone="13800138000")
# username → 'alice'（先裁空格再转小写）
```

> ⚠️ `pattern` 是 **`search`**** 语义（部分匹配），不是 ****`fullmatch`**。实测 `Field(pattern=r"\d{3}")` 下 `"ab123cd"` **通过**。要整体匹配必须自己加锚点 `^...$`。

**语义化字符串类型**（比裸 `str` 表达力强得多）：

```python
from pydantic import BaseModel, AnyUrl, HttpUrl, SecretStr

class Contact(BaseModel):
    home: HttpUrl              # 必须是 http/https
    avatar: AnyUrl             # 任意协议
    api_key: SecretStr         # repr / 日志里显示为 '**********'

c = Contact(home="https://x.com", avatar="ftp://x.com/a", api_key="sk-123")
print(c.api_key)                       # SecretStr('**********')
print(c.api_key.get_secret_value())    # 'sk-123'   ← 只能显式取
```

> ⚠️ `EmailStr` 需要 `email-validator`，`pydantic-settings` 是独立包。本机 `E:\fastapi_learning\.venv` **当前都没装**，用到时先执行：`pip install "pydantic[email]" pydantic-settings`

### 4.3 集合与容器约束

```python
from typing import Annotated
from pydantic import BaseModel, Field

class Article(BaseModel):
    tags: Annotated[list[str], Field(min_length=1, max_length=5)]   # 元素个数区间
    scores: dict[str, Annotated[int, Field(ge=0, le=100)]]
    ids: set[int]                 # 自动去重，元素必须可哈希
    pair: tuple[str, int]         # 定长元组：长度必须正好是 2
    path: tuple[str, ...]         # 变长元组

Article(tags=["py"], scores={"a": 99}, ids=[1, 1, 2], pair=("k", 1), path=("a", "b"))
# ids → {1, 2}
```

要点：

- 容器上的 `min_length` / `max_length` 约束的是**元素个数**，失败类型 `too_short` / `too_long`
- 嵌套类型**逐层校验**：`dict[str, Annotated[int, Field(ge=0, le=100)]]` 会校验每个 value
- `dict[int, str]` 的 **key 也会被强转**：实测 `{"1": "a"}` → `{1: 'a'}`
- `set` 会丢顺序且要求元素可哈希；需要「入参可列表、内部存集合」用 `frozenset`

### 4.4 字面量、枚举与联合

`Literal` 是最便宜、最推荐的收窄方式：

```python
from enum import Enum
from typing import Literal, Optional
from pydantic import BaseModel

class Role(str, Enum):          # 混入 str，序列化时直接是字符串
    ADMIN = "admin"
    USER = "user"

class Task(BaseModel):
    status: Literal["todo", "doing", "done"] = "todo"   # 只能三选一
    role: Role = Role.USER
    remark: Optional[str] = None    # 可为 None，且可省略
    note: str | None = None         # 等价写法（Python 3.10+）
```

- `Literal` 校验失败类型是 `literal_error`（实测）
- 枚举写成 `class X(str, Enum)`：`model_dump_json()` 出来是 `"admin"` 而不是 `"Role.ADMIN"`；也可用 `ConfigDict(use_enum_values=True)`
- **`Optional[str]`**** ≠ 可省略**：`Optional` 只表示「值可以是 None」，**没有默认值就仍然必填**。实测 `class F(BaseModel): s: Optional[str]` 调用 `F()` 报校验错误。可省略必须写 `= None`
- 联合类型默认是 v2 的 **smart 模式**（按输入形态智能选分支，而非从左到右盲试）：实测 `Union[int, str]` 下 `"12"` 保持为 `'12'`、`12` 保持为 `12`。要改回顺序匹配用 `Field(union_mode="left_to_right")`

### 4.5 日期时间、UUID 与网络类型

```python
from datetime import date, datetime, timedelta
from pydantic import BaseModel, UUID4, IPvAnyAddress, PastDatetime, FutureDate

class Event(BaseModel):
    created_at: datetime
    past: PastDatetime       # 必须是过去时间
    deadline: FutureDate     # 必须是未来日期
    duration: timedelta      # 也接受 "PT1H30M" 或秒数
    uid: UUID4               # 校验必须是 v4
    ip: IPvAnyAddress

Event(created_at="2026-10-05T10:00:00", past="2020-01-01T00:00:00",
      deadline="2030-01-01", duration="PT1H30M",
      uid="b3b1b1b1-1b1b-4b1b-8b1b-1b1b1b1b1b1b", ip="127.0.0.1")
```

其他可直接用的类型：`UUID1..UUID8`、`FutureDatetime` / `AwareDatetime` / `NaiveDatetime`、`IPvAnyNetwork`、`FilePath` / `DirectoryPath` / `NewPath`（新建文件用）、`AnyHttpUrl` / `PostgresDsn` / `FileUrl`。

### 4.6 嵌套模型与自引用

```python
from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    detail: str = ""

class Order(BaseModel):
    addr: Address                                        # 嵌套 dict 自动校验成 Address
    items: list[Address] = Field(default_factory=list)   # 可变默认值必须用 factory

Order(addr={"city": "Beijing"})    # addr → Address(city='Beijing', detail='')

# 自引用（树形结构必需）：字符串前向引用 + model_rebuild()
class Node(BaseModel):
    name: str
    children: list["Node"] = Field(default_factory=list)

Node.model_rebuild()
```

> 🔴 **可变默认值铁律**：`list` / `dict` / `set` / 模型实例做默认值**必须**写 `Field(default_factory=list)`。pydantic 内部虽然会深拷贝（不像裸 Python 类那样共享），但与 `dataclass` / SQLModel 混用时极易出错，**统一用 factory 是团队规范**。

### 4.7 别名与序列化控制

前后端字段命名不一致时用别名，不要手写映射：

```python
from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

class CamelModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

class User(CamelModel):
    user_id: int = Field(alias="userId")
    nick_name: str = Field(default="", serialization_alias="nickName")

u = User(userId=1)                        # 入参用别名
print(u.model_dump(by_alias=True))         # {'userId': 1, 'nickName': ''}
print(u.model_dump(exclude={"nick_name"})) # 排除字段
print(u.model_dump(exclude_none=True))     # 排除 None
```

- `populate_by_name=True` 表示**别名和字段名都能当入参**，改造兼容期必备
- `alias` 同时管入参和出参；要分开控制用 `validation_alias` / `serialization_alias`

### 4.8 严格模式（strict）

默认 lax 模式会强转，想要「类型不符就报错」：

```python
from typing import Annotated
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt

class A(BaseModel):
    x: StrictInt                                    # 字段级

class B(BaseModel):
    model_config = ConfigDict(strict=True)          # 模型级：全局严格
    x: int
    y: bool

class C(BaseModel):
    x: Annotated[int, Field(strict=True)]           # 约束级
```

实测 `StrictInt` 与 `Field(strict=True)` 传 `"1"` 都报 `int_type`。

**该不该开 strict？** 入参是 JSON / HTTP 时**通常不开**（`"7"` 转 `7` 正是后端想要的）；内部服务间调用、金额、ID 这类「错一点就是事故」的字段**建议开**。

---

## 五、跨字段与模型级校验

单字段约束不够时（如「结束时间不能早于开始时间」「两次密码一致」）用校验器。

```python
from datetime import datetime
from pydantic import BaseModel, Field, field_validator, model_validator, computed_field

class Booking(BaseModel):
    start: datetime
    end: datetime
    password: str = Field(min_length=6)
    password_confirm: str
    tags: list[str] = Field(default_factory=list)

    # ① 字段级：只关心单个字段
    @field_validator("password")
    @classmethod
    def pwd_not_weak(cls, v: str) -> str:
        if v.lower() in {"123456", "password"}:
            raise ValueError("密码过于简单")
        return v

    # ② before 模式：拿到的是原始输入，还没做类型转换
    @field_validator("tags", mode="before")
    @classmethod
    def split_tags(cls, v):
        if isinstance(v, str):            # "a,b,c" → ["a", "b", "c"]
            return [t.strip() for t in v.split(",") if t.strip()]
        return v

    # ③ 模型级 after：所有字段都校验完了，能拿到整个 self
    @model_validator(mode="after")
    def check_all(self):
        if self.end <= self.start:
            raise ValueError("end 必须晚于 start")
        if self.password != self.password_confirm:
            raise ValueError("两次密码不一致")
        return self          # ⚠️ after 模式必须返回 self

    # ④ 计算字段：不入参，但会出现在 dump / JSON 里
    @computed_field
    @property
    def duration_hours(self) -> float:
        return (self.end - self.start).total_seconds() / 3600

b = Booking(start="2026-10-05T09:00:00", end="2026-10-05T12:30:00",
            password="abcdef", password_confirm="abcdef", tags="py, fastapi")
print(b.tags)                              # ['py', 'fastapi']
print(b.model_dump()["duration_hours"])    # 3.5
```

要点：

- 校验器上的 `@classmethod` **不能省**
- `mode="before"` 拿原始输入做**预处理**；默认 `mode="after"` 拿已转换的值做**业务校验**
- `@model_validator(mode="before")` 参数是原始 dict，可返回 dict 整体改写；`mode="after"` 参数是 `self` 且**必须 return self**
- `raise ValueError("...")` 会变成 `ValidationError` 里的一条（`type` 为 `value_error`）；`assert` 语句抛的 `AssertionError` 同样会被捕获
- 想在字段校验器里读其他字段：加参数 `info: ValidationInfo`，用 `info.data.get("xx")`

---

## 六、`model_config`（`ConfigDict`）常用开关

```python
from pydantic import BaseModel, ConfigDict

class Base(BaseModel):
    model_config = ConfigDict(
        extra="forbid",                 # 多余字段直接报错（接口防脏数据首选）
        str_strip_whitespace=True,      # 全局裁剪字符串首尾空格
        validate_assignment=True,       # 赋值时也校验（默认只在构造时校验）
        from_attributes=True,           # 允许从 ORM 对象构造（原 orm_mode）
        populate_by_name=True,          # 字段名与别名都可作入参
        use_enum_values=True,           # dump 时枚举输出为值而非枚举成员
        frozen=True,                    # 不可变（可哈希，能当 dict key）
        arbitrary_types_allowed=True,   # 允许任意自定义类型
    )
```

实测：`extra="forbid"` 下 `J(x=1, y=2)` 报校验错误。

---

## 七、和 FastAPI / pydantic-settings 的衔接

### 7.1 FastAPI 里的三处用法

```python
from typing import Annotated
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field

app = FastAPI()

class ItemIn(BaseModel):                      # ① 请求体
    name: str = Field(min_length=1, max_length=50)
    price: Annotated[float, Field(gt=0)]

class ItemOut(BaseModel):                     # ② 响应模型：字段白名单 + 输出校验
    id: int
    name: str

@app.post("/items", response_model=ItemOut)
def create(
    item: ItemIn,
    q: Annotated[str | None, Query(max_length=20)] = None,   # ③ 查询参数约束
    item_id: Annotated[int, Path(ge=1)] = 0,
):
    ...
```

- `Query` / `Path` / `Body` / `Header` 的参数签名**和 ****`Field`**** 几乎一样**（`gt` / `max_length` / `pattern`…），因为它们共用同一套约束体系 —— 学一次到处能用
- `response_model=ItemOut` 会**丢掉未声明的字段**（防密码泄露），并做输出校验
- 校验失败 FastAPI 自动返回 **422**，body 里的 `detail` 就是 `ValidationError.errors()` 的列表（`loc` / `msg` / `type`）—— 所以会读 `errors()` 就能看懂接口报错

### 7.2 pydantic-settings 读配置

```python
from pydantic import PostgresDsn, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    PROJECT_NAME: str = "learning-record-api"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PASSWORD: SecretStr
    SQLALCHEMY_DATABASE_URI: PostgresDsn | None = None

settings = Settings()      # 缺必填项 → 启动即报错，而不是运行到一半才炸
```

> 📌 **对接 W0**：精读模板 `backend/app/core/config.py` 时，重点看 `Settings` 类里每个字段的类型与默认值 —— 它和 `.env` 的键必须一致，这也是 `docker compose` 报 `${POSTGRES_PASSWORD:?Variable not set}` 的根因所在。

> 📌 **对接 W1**：给 `LearningRecord` 写 `schemas` 时，创建 / 更新 / 输出**三个模型分开写**，约束（如 `duration_min: Annotated[int, Field(gt=0)]`）只放在创建模型上 —— 这就是模板 `items.py` 的做法。

---

## 八、常见坑清单

**读 ****`ValidationError`**** 的标准姿势**：

```python
except ValidationError as e:
    for err in e.errors():
        print(err["loc"], err["type"], err["msg"])
    # ('password',) 'string_too_short' 'String should have at least 6 characters'
    # ('end',) 'value_error' 'Value error, end 必须晚于 start'    ← 自定义校验器
```

---

## 九、速查表

> 记住 v2 的四个入口就够应付 90% 场景：**`model_validate`**** 进、****`model_dump`**** 出、****`Field`**** 约束、****`model_config`**** 定行为。**

---

## 十、自测题（对照学习计划）

闭卷写完再对答案，每题 10 分钟内：

1. **（W0）** 写一个 `Settings` 风格的模型：`host: str` 必填、`port: int` 范围 1–65535、`debug: bool = False`、`tags: list[str]` 默认空列表；多余字段必须报错、字符串自动裁空格。
1. **（W0）** 说明为什么 `class M(BaseModel): x: int` 下 `M(x=True).x == 1`，并写出两种挡住它的改法。
1. **（网课 9–13 集）** 用 `Annotated` 定义可复用的 `PageSize = Annotated[int, Field(ge=1, le=100)]`，分别用在 `BaseModel` 字段和 FastAPI 的 `Query` 参数上，说出两者约束是否一致。
1. **（W1）** 给 `LearningRecord` 写 `Create` / `Update` / `Read` 三个模型：`duration_min` 必须大于 0，`Update` 所有字段可选，`Read` 要能从 SQLAlchemy 对象直接构造。
1. **（W3 预热）** 写一个模型校验 `start` / `end` 时间顺序，并让 `duration_hours` 以只读计算字段出现在 `model_dump()` 里；再触发一次校验失败，把 `errors()` 的 `loc` / `type` / `msg` 打印出来。

