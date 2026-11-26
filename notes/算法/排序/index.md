# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QC3JAR4P%2F20261126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261126T103014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFHJ7sXpxoOjxD0REdCjOH4SqBIz74xa2GBxkGsThnxgIgGwLTuz3XfbqUV3MUyOILJ9H%2BKHS%2FSefBxslUM5j8zLMqiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB5%2BvyiEq0eFfTLl%2FircA8obS7XKKCIxkJu3zOfOtGErOGqKyaHfy%2Fqwncg73mKw%2FHKrgVu1H6mO7xQ9rVM04YmyOKCdNkWm%2FSX8aTIDYD%2BWqMdLU%2BpdmiMBw%2BhlblT%2BBen4CmH7VVTin19e%2BPAgYgV9WTjop368L4gHSw63uMDiolR%2FEn2AQ4zciaYgTQL21Yo6OusJvzDfc6ZnbUydVESwj%2BGi9t9GMCelLM7BZcrTrVrJ6U6a5XGYz%2FmttOWtFsON6eP05RtFSYK0c7ZdTvrZAX6v3b32GKQsXxtZTCJXaizCJoalnD%2F51ZwXFojN1kWlPUmj5%2F%2BVTYhtHeZipIHjBIka5msV6qGdXfwofGLTOOq%2BLgnerQ9gFKSe0o80w3W4STjGfuPq10QM2FaHv%2BT1NOFjfgT4EUpjl5%2F26RfaGRaNLkMdKJ5E0Ww%2FPNbgIyngnBtRFZ8kZwaEqVRqyGBKZLKemvSL4zd13D0RW2tlq29cqgPU3RQzXKy8dT%2BykkWXxpaM581xe48tOxPqv9Xfj3GrYmtm9ciOBPTgySbtlnt1O0rvg3N3f%2BCLcioNOJKrIP0TfiE7LNf1Y3sx1vdsVz1OrP9Cip6opAhkUxL95G2lFVm%2FkiCnXNF21j1jajH6lhu9RbeurVlsMPTuntgGOqUB8tTw%2F0n6l3iuy2wIV7cPrrviF%2BTr6gmO45x6ZFrhCDifxb1bg9P3RXB5%2BNMSSn9rSUop8uFegrCYnehakyfdpIopwUJYhqtl3fz%2BlFDGaRezo5t0sWcCLi9zwodVfs8ax29GZVpx%2Bdfz46rk2BrPBupv2RsGMj18mw94L5QwJWVVHLcqnVbE%2F%2BfC6%2BqO2AUHi7GOpMhAh58VncLZ3y3Np%2FN%2By%2FlC&X-Amz-Signature=e71ff05371224d302a550d5da95d4e96e489248104564ecf5d38afba55211a16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







