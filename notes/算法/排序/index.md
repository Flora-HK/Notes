# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIZDKGFY%2F20261009%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261009T083222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJHMEUCIQDEILbflMHZNeWEzNDv79Gj8%2FhPu%2Fpmy%2FNX6myU35hK5wIgaMD0pguUzHgGIh%2FaB5PMG4nfdtKZm%2B%2FWUqL%2BGnPNb4sq%2FwMIOhAAGgw2Mzc0MjMxODM4MDUiDGtSDMgQynfhCfNfOCrcAx%2BLOd3b5ewxR89MdwNmSP5gUO8KC%2BAYxmrrL7MKJANrHU%2B8XglZVo7HcukAZuRoNktrX%2BOCH9ovvgApk%2FE3LRAVyZw4pTKdi3T2KTffdmveT9DDW9Gfuh00c0hOAKK4%2F9otWg8MLZV0GqZFESgzHHqjkYhE47tlW%2BupSJQ5Dzxvyg2EL7USM7k7jsJg3gzJPE%2Bw1vjbF2VE3yJ%2BAGcfmmLL1h87E5f7cRu7riNhTP44mVKAVHkOMvo8nmyyG4TXt68SW0EFIONOspwOkvjyEnmyGw0wNUSVEjaLkUU3lUnBW5CKpgOrD%2BPzYcIg4ERwvysYkTP574h8KS21J6KxeYWdbx8KvCPPMxnkMY04U4kAHkz2sSlnOkkhiByZYBF5HbhFbpUc40E%2F2b5%2BzNBkWrUBgdtoHbLSXiyFtK5dgZb4l9RkHZxxxXKCipBmwdpdjP%2BrN7YEZc%2FW0h6lCZRUQgSn%2Bs8gSYT%2F1UlBPdv%2FAuBVUxLZ65a5KAp%2BdGtjeVakAz%2B5hOIYuymmuxtjU3ykkO5fX9dSNADWgehZOgN48y5kGFptPZZIxXQoefVIs49llkYjHbskcM8sSRR0N3Y%2BcT2yosHq%2B1UJENptbRDlocu3TjroNDMNG9rTaZjnMNHMotYGOqUBU%2BX2kp2%2FMOh320g0K%2F%2BGmq8yF6316TXYC%2FQnarJOlp6epeKfoXNCIoV1JonXlnVtEV2hbdjzXRiGzXwOoNzx1udwaNuNi7Lk3sB2KxYQRCmOuwtYnNuNxwnS76OUekl%2BTml%2FpW16ss9f0m9qaqwjZVVwdwg88HQTug%2BkKyHkf1oqu96cRtf07IiBiXLtMrqK9FmXpYw8w4U9bnBbdPzg8Rb4CK08&X-Amz-Signature=ef4523a2bd481a5eda08d0079771777c8f6e8892403bd17c8bfb8dc5f421b818&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







