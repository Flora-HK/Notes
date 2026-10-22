# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676VMRSTI%2F20261022%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261022T071034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCo3oyX3soaN4A03xkNmDcaD2GRcvFj6BHEEYdM8tmtUQIhAN8HEEuMB8UmyJ%2FX3vN3pPqSzc2waVfkHjg2cTIuB9hwKv8DCG4QABoMNjM3NDIzMTgzODA1IgxW3OQhQbxRT3ehEVEq3APiWInTmecko0dlqIUMKGrKA0EOEhtok0fXnhsg13YwKQYfOS74kOW6QZK85MYTrU8G%2Fv935PFXYuQKN8Nx84bLqgDQnN4g9yipCheKtUeCIjugc7dY4%2FvgqCJKpW2FjXqBSsQ2IeYtkPdSBdRTkOjJr8jWMoY2SrypkOj7MNeAtYyOH%2BZtk98A0ODQ9V2buO6ZLQ921gzIHYVTlzoqbbBZNcny8ermtMW47NyW0vEphW%2F0Cqrk3EaZxm4XyHh%2B7fYj82CmkBF6V9ceIohvaYb%2BGOUYWp%2B013Wd1NyCd6IYBxcU5eRH9Ot157BKv06LLMyAI1J8gixppDvRlXoEsOamrJZM7h5D9crSpGHEYrnz4XVmteSRs4tO9aY04GkwfbtZv5gpMFbtSL%2BWwTA3kh0TfS%2FhbluhvsQRukgOtaepT1stp3B973%2Bj1X%2BTJnDrUq03pEIbe2KL%2FvjH9%2FnM921T27%2FwuCwner4Qeal1MrbarDIF2m78YOstsR5wqw91a0vplFjx2WfXPPQqBNGFJWvSaH0cj2zYbb0rpGU%2F6aeDaf0lsjeyVIrlpS71tr%2BTeQNLTCupmOZTSt5MXKKHD1MnLYJEn5GgYtpSxpjDpNvMsazAXnCUuXIYw2zb%2FzCrz%2BbWBjqkARr6iaULQ6%2BIHBbL9eJgz7QOSek2%2B60kaPvWWjq016F2skUMgE30mB5Nqc7Dajt0a%2BWzIBmrdEV3bYEQKpCidpgPrxfERQF4tV6LBoDWtORyDUY%2B27yrYxH5pDD7tQL2vSP%2F6lpVR8d%2FW4ljQ5l1%2BL%2FkLt%2B3c2k2JkNJ4vwR4k42cpYgCTKEx%2Fb0EyF47cl59flfXeaKCgNa4w%2BfpG66tIfPu2JB&X-Amz-Signature=7a30f7479f905922bd8acd6609d8d8bb55c73458e85908d6b28e117ac6c4ea04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







