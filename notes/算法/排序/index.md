# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NBDVBHI%2F20261012%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261012T084230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2BZ%2FuHTuc3zY8gAgmuSn9PIgx6MRWqL0nCXPpYfyS8kAIgR7bX9icPjZzRnwvqRyowUMNKcQ5Ssea%2FkB1fEC%2F5gOoqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOJE0a145nT3irZpFSrcA%2BNoYOGmUFOGS59aaYcCGwvaTsWL0SoC7YOVe7l%2Fzb19x9Sh8%2BdilyjXP7853b1wxF4BZLXz4%2FX%2BGOLDQFFnX3PH1lUYOe5W918AdvmJcf2akc%2F4TjLwHC8RvnzDnR0bpOaPp09cxVNjarKU8xhvaY53qkKyKwLrzD00J1DwzECjQV7vD5MEOosx8vCiNrQVSOCXhx6PKiv6h8N1iLuzAIO2S5zSRMishfGxm4dYOlqja8rJvnf8WDdE2dODSEBHM667qvTBogW4ap3AywnuD0t5ktTzWNpcGh031pkda0XiestxKpR5qBMI%2FTZhzPVebSt1adOxeWnLO0nsz4aeVIwaZW64dp4oQ7UT5KVJQa6lsDptktimAEhe45aYCG9WfX%2BJaHDccTZJUVv7DCXAUoVsndaxY0iImpECFuY1glge3fPbXl7x0HEhPNxR8pQJYUWEU8cqCG1NvsDOuZwLPSCp7h6BEpYezBOHpOYNtFqn0arD1ZBnp6dDKJ5uJUhHmBLRQz%2FkemAoYO6WmS7YRjCPvcz9SXfgugkvjv8o3tDbIyH6YK2TQj3cczaOSOk%2Fleg79DPW82JFkJJkm60v0Owlo0CNsFXdZJbpAla626btKbdiOuVOA177JWfyMPyvstYGOqUBQ848R9lA%2FCY1ZxVeR5cKWLnOLpqzrRaacN4FKwpmru1S3NC8kYUG2lmzwZjBJTd40DNka4r37VwsLlEOsaaUBvkJ%2FJnOQpFQp4vNX7lO035RWFEqSyfJ37TVCqkJ1SgFcz%2BOjDXKId%2BnPPQrTyZHjWKKw9WgOoB5zjkbwfePdcs3zYk4vEqNxseBjGvvGRmQjAReHjkEaiJNszNZwajmS66LXFQ0&X-Amz-Signature=542ca0b3eea75612596a459f6eeb1e3f8f859f381478f819cdf3a3bf54988a05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







