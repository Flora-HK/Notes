# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJW3CIUU%2F20260928%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260928T081740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEb%2BH6pUARvR1hYsbbQBhWaL5Urx3Nn2ukFBDDTMLcgAAiEAm%2Fgwnw34K6ZrrG374N9fL6Q7qwpSiFX9UuaRm2oERhsq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDB7q6iyaZ8sEmzOtkCrcAy1iF5yCYVLxbcsUcs3M%2FtYrDSDXZSfaBVOhDIPnzs2g0lHadNKHc6rb3Wofdw7Gtv80D5tqrMF12J0qqYvANPNLxKpBryrSfpZ83nBMSkqDww39HxqiGjLL%2Fuf0%2F%2BCznVc7UFhFT%2BXdQIhYPK4D9e5RXDLS2g15WwLuMPJYdToh476xaAZ2UzctZjZ8v8AIVHRJdLHo58NBRH8FuYY8hTcT2ScD8BvinmV9vDJ2ZvGDcbSxKZQ0YAmXatDuxZhmPlqFPzMrmu%2BSB3bTbyW%2FnKEZU9dOUihgnwRJJdmPwXw66s3mTcn4s4XL8617AE%2BeBGYK%2FM%2Fn9zxIU6rSeL1uTeZHn9wjbFr6L4VetAxV7EyBLoqRvn13ciLq42I4lLdMWWQKjx8qh5WFMYX0%2FPuWgbp6uzpK96ql%2F5dQbJ18OElAUwSUAEdSNwmUzuMZaj8N6v4aVz5u7hF9TphPGJFGQsWxnPFYNDWPv2GT13XmefUxZ6N3mgKYozrsA%2Ft2hYvB7rzamamdjezIE3z%2FqfetxMOZCbQZnuG7bDznMeQw%2B0kLYdw9u0%2B6H84qnqPkCYkhfiGW4MrDexqZKE65sTrmKvcIhN8pA%2BHC%2Bn5jTId3iFirjcZPjMjVgN2D76sfMIfx59UGOqUBKTtjQIxeuaN1wmjNV4U%2BX6OheumXDkfvkvtpW9v1JDsmhbGLLz6kJ0l5eu%2FiJllDHdf95nCXUUiNNBUu%2BICM%2BdYq8D6U41lm5U2s5lWsDOwqA8G1odgF4JA7xOrg0rldPkSMK3SX9HUnLq832VPpSDpgRxtHxJL0u7ZcGF1jQRLfSDzvsRak2OlubG51YP2Yyi0mhlQMcApDwUD4JsKe3aPVo8T1&X-Amz-Signature=72a79d9a7cdc645f6d98057322692c7e129bc4bc1b4ae834833503ff87de7e2f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







