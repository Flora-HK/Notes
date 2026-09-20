# Collections 模块

一、  `OrderedDict` ：一种带有特殊方法的有序字典，有两个常用方法：

```python
d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
d.move_to_end('a')      # a 被移到最后
print(list(d.keys()))   # ['b', 'c', 'a']
```

```python
d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
k, v = d.popitem(last=False)  # 弹出最旧的 'a'
print(k, v)  # a 1
print(list(d.keys()))  # ['b', 'c']
```



