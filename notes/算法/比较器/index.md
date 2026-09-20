# 比较器

对于所有的比较函数 `func()`，可自主传入某个比较方式，该比较方式称为比较器，实现方式为定义某个函数 `comparator()` ，该函数内容可以自定义，其中比较函数 `func()`通过接收 `comparator()`返回的比较结果来控制 `func()`的比较排序策略：

（1）`comparator()`返回负数的时候，第一个参数排在前面

（2）`comparator()`返回正数的时候，第二个参数排前面

（3）`comparator()` 返回0的时候，二者相等，谁排在前面无所谓

比较器的使用：

1. 比较器的实质就是重载比较运算符
1. 比较器可以很好的应用在特殊标准的排序上
1. 比较器可以很好的应用在根据特殊标准排序的结构上

Java 中常用 `Comparator<T>` 作为外部比较器，`compare(a, b)` 返回负数表示 `a` 在前，返回正数表示 `b` 在前，返回 0 表示相等。对象数组可以用 `Arrays.sort(arr, comparator)`，集合可以用 `list.sort(comparator)`。`TreeMap`、`TreeSet`、`PriorityQueue` 也可以接收 `Comparator`。如果类自身有默认排序，则实现 `Comparable<T>` 的 `compareTo`。
在其他需要用到“排序”的方法中，也可以为方法传入该比较器 `comparator()` 来控制其比较策略

在Python 3 的 `sorted` 和 `list.sort` 主要使用 `key` 函数，把元素映射成可比较的键。若想使用上面这种三态比较器，可以用 `functools.cmp_to_key` 把 `cmp(a, b)` 转成 `key`。

```python
from functools import cmp_to_key
arr.sort(key=cmp_to_key(cmp_func))
```

`cmp(a, b)` 返回负数表示 `a` 在前，正数表示 `b` 在前，0 表示相等。

在C++中，比较器是可调用对象，返回 `bool`，表示第一个参数是否应排在第二个参数之前。例如：

```c++
std::sort(v.begin(), v.end(), [](const T& a, const T& b) {
    return a.key < b.key;
});
```

重载 `operator<` 可提供默认比较方式，但比较器本身不等于“重载运算符”。C++ 比较器必须满足严格弱序。



