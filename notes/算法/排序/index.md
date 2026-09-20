# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEAVYHZ6%2F20260920%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260920T071413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGuXY4jLYgatA3F65R%2BqE4YENJrYa8tRml3FUgvGACJgIhAP8HGNDgXOvnWcWx%2Fio6W8nNxXj%2FK6PSPUyENwRXPyA4Kv8DCHAQABoMNjM3NDIzMTgzODA1Igy7JO37Pvs2FfWCh4Mq3ANlH2Q5U3VvRPD2F6OgqCSFxlJIZtshlaNFSXKk2a8EiVZfGA6SEXjpcYsK4PPTDWez9ymgMYt63wsNRln%2BEGOkpNRtmMAjw2mgRFgnInPi6ZyNR12cwCWQaZ7AJH7W%2FHUJOqtubgGn8ptXwaqMMAYa8ltZz2klJRcHWDOirHHDalDnYag98SS8w26Cs6QtsJRlL%2FkP08UWcLOU2Iks3YPngPCqK0n7A6HysMQ0PL3n3kmSOIbKOqIFg9iKGye4dz23MYmPAjOfeYlkKN%2ByaqFcW%2BefOj8uX3xgHMsEyohajNapiUy8CfT4yuluLnHG4XVkxpM%2B0SVXakhTecFo2TyeL7laHcDrr3Ra2A%2BG9G3f7OagAuclMV59AzDUfOITHykPYaOogTY5%2FftlXS%2F%2B5mb8xCrGjE%2FqrzeuXk5oLmV2XbpAUrQf9ArCuEBnZB3izQnayM7in7NYAgPcuINpMcf3E04Qa%2FQu2QDXOLQtUBHRI2TP3HgIAENSdQokA9p%2BDE9obL%2BU2waXZVUX451gjtAPre69O1t9hWeQoHfsQWa78rsRb3sdUDb%2BaPD%2B7bEImLa%2Bv5seUHmBHHaoiPFBsJydgk%2B4RXThxUuTMgdxApfUhPctq69UWRAWx2VrcjC%2F%2FL3VBjqkATu7F%2Bj8wpCDNG5tMpOv8Vly0M8qphe4VaR5pJaIv0mglqfRiaHIL2s2Y63%2B1pOfMT6MaazMk75OUV%2Fwc8ZUbFaNG8bqRdHsRqaIGjrN53vF25SB5UiCq5WLMWC9GDeKRO7mWPcb1lZnqC9PXURGB802%2Bgsi8cU7XDXI5dU7VP00PI2AR5jrYg6Jm63%2BxJjo7o7J4eOP8BLuGAF0UxBIDhWfZi6o&X-Amz-Signature=2e8dda7085d1c3740514a1bc260ee792e32e3b42c0cc0bb4b5391b0513986886&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







