# path 模块

### 1. 什么是 `pathlib`？

`pathlib` 是 Python 3.4+ 引入的**面向对象路径操作库**，是 `os.path` 的现代化替代方案。一切皆 `Path` 对象，而不是字符串。

**核心理念**：
- 旧方式：`os.path.join(base, subdir, filename)` — 字符串思维
- 新方式：`base / subdir / filename` — 路径对象思维，更直观

### 2. 创建路径对象

```python
from pathlib import Path

# 当前工作目录
cwd = Path.cwd()
print(cwd)   # e:\Codework

# 用户主目录
home = Path.home()

# 直接创建
p = Path("e:/Codework/data.txt")

# 用 / 拼接路径（推荐！）
base = Path("e:/Codework")
json_file = base / "data" / "students.json"
print(json_file)   # e:\Codework\data\students.json

# 字符串与 Path 混合拼接
download_dir = Path.home() / "Downloads"
project_dir = Path.cwd() / "project"
```

> 💡 **技巧**：使用正斜杠 `/` 拼接，`pathlib` 会自动适配操作系统路径分隔符。

### 3.  路径信息获取

```python
from pathlib import Path

p = Path("e:/Codework/project/data/report.xlsx")

print(p.name)       # report.xlsx      文件名（含扩展名）
print(p.stem)       # report           文件名（不含扩展名）
print(p.suffix)     # .xlsx            扩展名
print(p.suffixes)   # ['.xlsx']        多级扩展名
print(p.parent)     # e:\Codework\project\data   父目录
print(p.parent.parent)  # e:\Codework\project     祖父目录
print(p.parts)      # ('e:\\', 'Codework', 'project', 'data', 'report.xlsx')

# 修改后缀
new_p = p.with_suffix(".csv")
print(new_p)        # e:\Codework\project\data\report.csv

# 修改文件名
new_p = p.with_stem("summary")
print(new_p)        # e:\Codework\project\data\summary.xlsx
```

### 4. 目录操作

```python
from pathlib import Path

# 创建单层目录，存在也不报错
Path("output").mkdir(exist_ok=True)

# 创建多层目录
(Path("output") / "images" / "thumbnails").mkdir(parents=True, exist_ok=True)
# parents=True  → 类似 mkdir -p，自动创建父目录
# exist_ok=True → 目录存在不报错

# 遍历目录（只列当前层）
base = Path("e:/Codework")
for item in base.iterdir():
    if item.is_file():
        print(f"[文件]{item.name}")
    elif item.is_dir():
        print(f"[目录]{item.name}")

# 输出：
# [文件] exp3.py
# [文件] exp4.py
# [目录] project
# [目录] python在线笔记
# ...
```

```python
from pathlib import Path

base = Path("e:/Codework")

# 匹配所有 .py 文件（当前层）
for py_file in base.glob("*.py"):
    print(py_file.name)

# 递归匹配所有 .md 文件（包括子目录）
for md_file in base.rglob("*.md"):
    rel_path = md_file.relative_to(base)
    print(rel_path)

# 复杂匹配
base.rglob("test*.txt")      # 以 test 开头的 .txt
base.glob("exp[0-9].py")    # exp0.py 到 exp9.py
base.rglob("**/data/*.json")  # 任意 data 子目录下的 json 文件
```

**`glob`**** vs ****`rglob`**：
- `glob(pattern)`：只在当前目录匹配
- `rglob(pattern)`：递归匹配所有子目录（等价于 `glob("**/" + pattern)`）

### 5. 文件读写

```python
from pathlib import Path

p = Path("data.txt")

# 读取全部文本
content = p.read_text(encoding="utf-8")

# 按行读取
lines = p.read_text(encoding="utf-8").splitlines()

# 写入文本
p.write_text("Hello, pathlib!", encoding="utf-8")

# 追加写入
old = p.read_text(encoding="utf-8")
p.write_text(old + "\nNew line", encoding="utf-8")

# 读取二进制
bytes_data = Path("image.png").read_bytes()

# 写入二进制
Path("output.bin").write_bytes(bytes_data)
```

> 告别 `with open(...) as f: f.read()` — pathlib 一行搞定！

### 6. 文件与目录判断

```python
from pathlib import Path

p = Path("test.txt")

p.exists()       # 路径是否存在
p.is_file()      # 是否为文件
p.is_dir()       # 是否为目录
p.is_symlink()   # 是否为符号链接
p.is_absolute()  # 是否为绝对路径

# 获取文件信息
stat = p.stat()
print(f"大小:{stat.st_size} bytes")          # 文件大小
print(f"修改时间:{stat.st_mtime}")            # 最后修改时间戳
```

### 3.7 文件与目录管理

```python
from pathlib import Path

p = Path("old_name.txt")

# 重命名（可同时移动）
p.rename("new_name.txt")
p.rename(Path("backup") / "archived.txt")

# 删除文件（目录非空无法删除）
p.unlink(missing_ok=True)
# missing_ok=True → Py3.8+，文件不存在也不报错

# 创建空文件
Path("new_file.txt").touch()

# 删除空目录
Path("empty_dir").rmdir()
```

### 3.8 综合应用：目录扫描器

```python
from pathlib import Path

def scan_directory(directory_path):
    """扫描目录，按扩展名分类统计"""
    stats = {}

    for file in Path(directory_path).iterdir():
        if file.is_file():
            ext = file.suffix.lower() or "(无扩展名)"
            stats.setdefault(ext, []).append(file.name)

    # 打印统计
    print(f"目录:{directory_path}")
    print("-" * 40)
    for ext, files in sorted(stats.items()):
        print(f"{ext:.<15}{len(files):>3} 个文件")
        for f in files[:3]:  # 每种只印前 3 个
            print(f"  └─{f}")
        if len(files) > 3:
            print(f"  └─ ... 还有{len(files) - 3} 个")

# 使用
scan_directory("e:/Codework")
```

## `pathlib.Path` 常用方法大全

---

### 一、路径信息获取

```python
from pathlib import Path

p = Path('C:/work/project/archive.tar.gz')

print(p.name)       # archive.tar.gz
print(p.stem)        # archive.tar
print(p.suffix)      # .gz
print(p.suffixes)    # ['.tar', '.gz']
print(p.parent)      # C:\work\project
print(list(p.parents))  # [WindowsPath('C:/work/project'), WindowsPath('C:/work'), WindowsPath('C:/')]
print(p.parts)       # ('C:\\', 'work', 'project', 'archive.tar.gz')
print(p.anchor)      # C:\
```

---

### 二、路径判断

```python
from pathlib import Path

p = Path('contacts.json')

print(p.exists())      # True / False
print(p.is_file())     # True / False
print(p.is_dir())      # True / False

home = Path('/home/user/docs/readme.md')
print(home.is_relative_to('/home/user'))         # True
print(home.is_relative_to('/home/other'))        # False
```

---

### 三、路径操作与拼接

```python
from pathlib import Path

base = Path('project')

# 路径拼接
print(base / 'src' / 'main.py')     # project/src/main.py
print(base.joinpath('src', 'util')) # project/src/util

# 替换文件名
p = Path('data/config.json')
print(p.with_name('settings.ini'))  # data/settings.ini

# 替换扩展名
print(p.with_suffix('.yaml'))       # data/config.yaml

# 计算相对路径
a = Path('/home/user/docs/readme.md')
print(a.relative_to('/home/user'))  # docs/readme.md

# 解析为绝对路径
cwd = Path('.').resolve()           # C:\Users\xxx\current_dir
```

---

### 四、目录操作

```python
from pathlib import Path

p = Path('project')

# 列出所有子项
for item in p.iterdir():
    print(item)

# 匹配一层内的 py 文件
for f in p.glob('*.py'):
    print(f)

# 递归匹配所有层级的 py 文件
for f in p.rglob('*.py'):
    print(f)

# 创建多层目录
Path('a/b/c').mkdir(parents=True, exist_ok=True)

# 删除空目录
Path('empty_dir').rmdir()
```

---

### 五、文件读写

```python
from pathlib import Path

# 读取文本
content = Path('readme.txt').read_text(encoding='utf-8')

# 写入文本
Path('output.txt').write_text('Hello World', encoding='utf-8')

# 读取字节
data = Path('image.png').read_bytes()

# 逐行读取（用 open 获取文件对象）
with Path('large.log').open('r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
```

---

### 六、文件状态与操作

```python
from pathlib import Path

# 文件信息
st = f.stat()
print(st.st_size)      # 文件大小（字节）
print(st.st_mtime)     # 最后修改时间（Unix 时间戳）
print(st.st_mode)      # 权限模式
print(st.st_ctime)     # 创建时间
print(st.st_atime)     # 最后访问时间

# 创建空文件
Path('new.txt').touch()

# 删除文件
Path('temp.txt').unlink(missing_ok=True)

# 判断是否同一文件
a = Path('data/data.txt')
b = Path('data/../data/data.txt')
print(a.samefile(b.resolve()))  # True
```

---

### 七、路径类型转换

```python
from pathlib import Path
import os

p = Path('C:/Users/zhangsan/docs/report.docx')

print(str(p))                # C:\Users\zhangsan\docs\report.docx
print(p.as_uri())            # file:///C:/Users/zhangsan/docs/report.docx
print(p.as_posix())          # C:/Users/zhangsan/docs/report.docx
print(os.fspath(p))          # C:\Users\zhangsan\docs\report.docx

print(Path.home())           # C:\Users\zhangsan
print(Path.cwd())            # e:\Codework
```

---

### 方法速查表（按功能分类）

```plain text
路径信息：  name, stem, suffix, suffixes, parent, parents, parts, anchor
路径判断：  exists, is_file, is_dir, is_absolute, is_relative_to
路径拼接：  /, joinpath, with_name, with_suffix, relative_to, resolve
目录操作：  iterdir, glob, rglob, mkdir, rmdir
文件读写：  read_text, write_text, read_bytes, write_bytes, open
文件管理：  stat, unlink, rename, replace, touch, samefile
类型转换：  str, as_uri, as_posix, fspath
类方法：    Path.home(), Path.cwd()
```

---

### 一句话总结

`pathlib.Path` 把路径操作从字符串拼接和 `os` 函数的散装调用，统一成面向对象的链式操作。**路径属性用属性访问，路径判断用 ****`is_*`**** 方法，读写用 ****`read_*/write_*`****，遍历用 ****`iterdir/glob`****。** 现代 Python 代码中，能用 `Path` 的地方尽量不要再用 `os.path` 那一套了。

