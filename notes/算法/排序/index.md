# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJBTVLO4%2F20261110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261110T092050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIE%2BbsHftxdYind68scv0aryhMJaiUzS8MYF8qNlIGNbPAiAxjLuoFAgCirGosgVyddrkRTxe9krTjJTdluey1g7IRyr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMKcLcLKfk6E1f%2BomrKtwDaYSXOroYo9%2F4lNMQV1bBCURs103gn3CI5A9hrZDyjSi16vNPep27OQrsBfuCX211%2FC3rzLzG6SA3NVwHYe0ShaviH0kGsG8R4VrMB3t7GHqbxtO6Sc6hd7njq3%2Fpkrj1ZpEaE1nh2cJLM4cGarn6PG9npjrcPm7mp5eTFRP%2F6Gp2Twc7ZTSW7pQ%2BgZcW%2Bki6RhXHaLuv9KBx3xhJprHJ31wj1j4W7gm9IP4GXUmkp0FpRHXZWQ%2Fp8ga3PPVhhvZG5lcYPBVEkxeDupN%2FWRV9GvuIfdT7F0zUvRl8AGQbo%2BWVbgsy9wI1eCf7%2F2dw4AXtru0ENux4d4K69UjCN0xeK5Jao9gpfNmVR2HVX%2BdAa6E4%2BDE%2BziEILphUtV89%2FIbwxCQK%2BsEpcjhAKNrMw6%2FKp%2BnywJJC9B5dHVvTtoiCknZS%2BME7DbfuiFJC1UA0y5R6XqKXu%2BIPakQ7ZoHYAdua2mN%2BF3wO2p1JWFq1bS5E6KeOe3K1a3E2FZrIFfMWtkkR9nGkWy3COcCzBsij2mWA7tc8m9MpqsO2m%2Fy3cDbyQRAc3vOrKa3RpQ45pfRWpukKL8QsNsZ3O0Xg00sIoaG4gyD0nfZy3lVMX28R1rT2SkOfKUQcT0kPYBDdkpYwkd3K1wY6pgFMgQgRlX1%2BFG%2B0grC%2BDfpZEsIv5jN3uG2X0TjE206NCwLfNxIC4zKrduVPqOwKb0z%2FkpaoxVWU%2BmABhJAzLP62VxFMczJZVOEjVvqoknTa0fAtT1592sdiPlo80OFt6%2BVkgmqhcCr86rhFOIwBoaUO7c4%2FrzOI7Zmq9YFe%2B3Y25Z2kSHxdVt7IS93J01Az4v9uNFfCXd54LtSU7zPSEjEWt2r8k4Ni&X-Amz-Signature=ef2b36397a415128272f2f41e13f4cdad8f20b28825111a89eceb1e040c30c32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







