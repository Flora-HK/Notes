# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SP5MH4I6%2F20261025%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261025T071913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIACmoRK%2FHHdwceqBJ7MLr%2FgVRss38UTmUCTdHOgv836JAiEA2UketCswAXqtZ4gxFb2B7%2BZ%2FmTDDH8wcXmmu5s1MyfYqiAQIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMlKxhtiZNhlD64zXyrcA78qRouLtr5Sz9KoVM3wzjAzZW1tRFs4FNj%2FsUqepgJNii0TqYpFIbBJMC0TiHHqBlKKIC4kL%2FIvQEFVzHvFc6TYn2xkWj8xNGJmVpIHqz51jE2UyeZpHt2jlkl5mTRzRR7TCQOJ4U20TwN4EWxy%2FIV4P%2FDWkxRgK835ZAwgN96y5n2wjqeVwsqok5%2BVotlXwb9PwfXYPLowHTrzw3rAAFSGthV5ImHTq%2FvXzlNVWfhp1DUJtKrpLthuNzV%2BQB8RIHZqcUV8msZrPiQjheYV1kHhb3k380go2Ko2mznL6TdpqPcbWgAPG%2B4%2BLSZcXiHgdPqE7YD3Vrobmz%2B0XWMrsCmellOgqxv0yAlFZJ4Nyx9bzSAn3wIVfV0FRD8IDWa%2FLwFcyiGYZa4UZ8KVfxbwmq8%2Fj%2BQGVzSuxwtORKWbsIskyFLBKH5cVmRkEzh2ns%2B96f64N7zio2SI68zePc5lEWGFxGmk8wwPF%2FT%2B8aNdt4yFqUMlfH4PMNP5Yr4D2X9Sy8swtyWVJEalfGcv1B6r6dtZ1QKxlP%2BXqASSXvPxGvERRwzt2FpYSRCDUokSnOvV5QIfZUMQHw4WNHuRCot5gxhJZIm5NJfRPQuxlyEuXdv9nfReaSumcOaS%2BctvMNO09tYGOqUBxIytCRv1wkq9fO8XY2alFt%2F1TkU1q50BDo6oic25ctubJEUH9R4Dy4OKsKujUr%2FFyMdGiitXG7%2BW7CM3XCK6bBn7qnUNZ4k4oIPU5Oho9PtAoB6CIG3tzzIjoOPIE6C4zTsE0thHBwyus0wJhuxgxzXlOrHJ2WRQa21zOiU%2B%2FxhNiXqfAau%2FEPdz%2FiFOPN2X2%2F6%2BnUctfexGZNMYfaVD%2FQeFAaj1&X-Amz-Signature=8d8a5c4d049f24532f4c7d2069652ed9ce90efde930dd70e205aeab1d3fdbcf1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







