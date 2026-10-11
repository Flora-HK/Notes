# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655KRSOJW%2F20261011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261011T082101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDh1JBwXGj2pe7QiV%2BN4ojha3ZYTG7W3wVXM9x6yUY84QIgR5IMLmPr0BISSucEIcRLLaN43PSaM%2FQ98mlgCjXSTFsq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDGxRdi2f%2F%2F%2FvQxGTJSrcA4cpGXWySGcDHYD5a0p%2FJN5PLSqWwNrZ7xlosljJ9Yie%2BXhGQ3l5pKzu1KCHJNqXl8lXHMTQMa87jAlo%2FuDLcx%2ByweAtUEZMMJD1sm%2Fol7kC3z4mH1rlnaZjqL7NWm5NvI8OzrI6McfTpOivqO%2F8ddni7VMYeiLSG2KNkhZ3Prmt3LqOXhYovAYc1NlGbQTRZlXb3I%2F6l8GFjW8kF7gvhKPuIXtGuA60TKXX3E7cDcwA13J%2FlMJOPVe%2FtQpsmMW7B6LRDsZ24rY7s%2FyawGBJ5Ggy907SVOjghmZlkq17ZSO9KiGpAH8jcYMXk%2B6DFENx9wc32I3Y7l487P9Udw%2B3BpPvm0y1ylcHpwHCNYynyMCb6eCkcozbJXhwPMht%2F7gxD32msFyBk5ylGoMGazFHT%2FfV2KVi4m9YNosGodUFdxjC%2BkzWZEpo3svAlMS0oKurAuzh8nGpqyiiIoLruMxVohOpeTjMyY7nzFPl4j65F5CfXt9%2BqA6W43rJauamg0Mz6j9%2BbeKEe2DYhqnb8z6WLwuFM58a5Fs%2BLu%2Bhr3FNLfDlz1xscnW2yDPJFy2iMhVm4GWuys1TgTo28%2FAqI80wClBKerZT33NSY4i86BXl9Et7ZFA%2Ba99QaYyP%2BNjdMMWxrNYGOqUBqPIhr1ecuWz7JHlX8iDfRD5alFtYZFAou3G%2B4RxwpsCGsY8cVpVqd1gYlTDjlQ7CrxMM5Rq0BxxT3lW0d5yCk8O6KCkKQ6%2FYgDhfiz1pata6K8qb4VWjixm1x7kF3nFNnqh5cG8bAtt1zGMqwsiGI3Dwj5u3gtBi4QJAJZuYCzn3T5zsi50dtb8OCZ7rW8etRwmz7GH6t4J37dq6BV4nowUsQV%2B%2B&X-Amz-Signature=8cb5114c123822667d605f490993e157ef59276f963fcfeaaf83a798b0a4bd85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

说明：

- `n`：元素个数。
- `k`：计数排序中的数值范围，或桶排序中的桶数量。
- `d`：基数排序中的位数。
- 稳定性：排序后相同关键字的元素相对顺序是否保持不变。稳定：保持；不稳定：可能改变。
- 快速排序的空间复杂度主要是递归调用栈，平均 O(log n)，最坏 O(n)。
- 希尔排序的时间复杂度与增量序列选择有关，因此不同实现会有差异。
- 计数排序、桶排序、基数排序属于非比较排序，通常对数据范围或数据类型有要求。

综合排序：在选择某种算法的时候，除了直接考虑时间复杂度和空间复杂度之外，还可以根据**数据量情况**来分层进行排序，在样本量较少的时候使用插入排序较快，在其他情况情况下使用其他排序；也可以根据**稳定性**进行区分：基础性数据使用快速排序，非基础性数据使用归并排序。

两大不可能：基于比较的排序不可能时间复杂度小于 `O(N*logN)` ；时间复杂度 `O(N*logN)` ，空间复杂度小于 `O(N)` ，具有稳定性的排序算法不存在

一、基于比较的排序：

二、不基于比较的排序：

三、算法稳定性：

1. 定义：对于一个待排数组arr，如果使用算法A对其进行排序之后，其中相等的元素的相对次序还能保证跟排序前一样，那么这种算法A就是稳定的。（对于基础类型数组没有应用价值，对非基础类型数组有应用价值）例如如下情景：
1. 符合算法稳定性的算法（直接进行较远位置的交换一般都不稳定）： 







