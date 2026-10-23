# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJTQMLUQ%2F20261023%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261023T070217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFkiT%2BOWBFdRbtZEP%2F5fON3uD43AVNFPzUYg9WQVROxpAiEA5zkVAIib%2F3f6RveIKXbMhZ2RX45ImiY5wqnuZcJjHA4qiAQIgv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIuLBG0exR4Zz7k8%2BSrcA4pYEzo26s2VxkFhFniAI9pwKK7O4Hp%2BrLslaQr8nWYfdUQrxegXDWmFY8%2B%2FPUJvWE0WXf9kZkGdFb2h4UyIzVpCYnMVGJYhkYLHykmM%2FulPYqO5mQZ71LFSjxFZwzjqZHUgTXAvlJ2epuUtmYbypKzGW5BpSj4TQV5uPdn1O2QndUmDsQcOycOozVWNv5TGz60lNCUPL3JCWlCoPnJ%2F4KSIbjrL5rrFo0iZtGSAxKDM6LXGCudpZsDaf%2B67tLo9PKvNFJ%2FDuGrTfz%2B%2BwTG8xyu1WSjLFFrLNdOWjfiYcFW1yEtQvSiswk7XImJfo7nXAwW5KV%2F907FttYEw21qoGDGadosDw0T0kycKzCBP%2BfDTHx5V%2FpVWu2%2Fri6xYCluXmQ78rjQM92DoAvCrlobPb0J5CUvaL6elo2KnDArT3aNkjprSFJXuMmCwFiDUlHK0q%2B5VxE1z2e7yrtVk6NE8Np%2B28lGmRD33Eqwz%2Be1HMWwYKE0YMRtFvVkTg5jjeYuSJNKzuzthEnj1qZBqu9Wy3y6kGgir1KU6zHfl6E1u9R8NvnuzHX7PujSAtLlNyksZBO7wUDVNJ5JK%2FlNaZIt3oBynAjjdT452LoAof%2BLcg%2FxubP7MPRt7PoY%2BVeE4MMCF69YGOqUB6CwW0Pz6QXgJ7r8DeMIFyOqV9bL%2Bv4Y3hM7gVcyGTvv5dV%2Fgef3g4a8aHdYollSYIj6HvFZ%2ByicnqV2PHqzhdOshuVKLP%2FYoJ6YliXQW1yKKr32KTDQbZ4fqwA3QEuXz3R7NIkHLqXQUfTU61sSKsJ%2Fbgg5NFfDZzuYG1TePCHiWsmFHFRsM9B%2BCVaBgnECq1DqI8WZxYw1qJ1ptN1W4Q9vPU9PK&X-Amz-Signature=be58b37c78c2e73b18eaecf2ee0bf47dfd3c3b5777436347469dd5132b10d0a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







