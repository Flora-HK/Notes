# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PRCXS3G%2F20261105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261105T090120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDGKlTFSKamKjKNmrGZ%2B57eKDW7AsudbrfSpXxhJSRA2AiEAn6XWJC9%2FMVuqe20qwFEKELv5GN5lpDBU1Z%2BHIwb5zi8qiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSc14FUZOwNwCY8WCrcA2hlLHlEVH5By42N2%2FXz97zPQ3cCSiKmnMWUFzFh4DLwBwseouoEep9AO4uU9SvqPFWzOdJW0O9qoozQKoBkGB%2Fz6B19PMpO%2Fsgweaxfx44nI0wsjpGuGmW%2FNo1XE2D0%2FYovt9tBfbamNYqCdVAyQ80AlY2wsurGg9lb8xmEGYafyoXroBnx7XulsLH3R04G9NsTT7ys1ikuotXoJPjA0XDS5ypq6ug4XyFNsk%2BeZ21JVUt2hyx%2FltHdrwB5%2BUlu5fb9fnngcc9VS1AggTqSEg63%2Bcfqhy1Jh31NrgAfzSSgEFaey8Yqi62s3edg%2FX8GC%2F8eclqbangPpyppPvFfUSNzI0FZWaJrhk3dgqIeWQ8gJnkTRaYAEwvPEd7UCJqr55dnLsLrmtiVE%2FWshBFbVU%2BCkt8oFJNeol0L1p1jQt8JRVz9lHIruHOBvJNmJMfEYZTKqwnxGQWLVtCH7heK8H%2FZqisQIU7diWEUAtJDj1D4Kck7TJoAVZc3y1SXQZAXHibJUP2Z7t20In%2Ff1LYGujLZUfCH8Ayd2D%2FVmDA5u%2BGw7XGAUpDrRI5xRbfivSOSiucGYR6aFtcklwgJwnG1acavRuY%2FxWmoEMn6BNUdZdPHD9dl1dgE4YwJAAc9MPrCsNcGOqUBudo54Qx7ipXzE1tPJSuzZCRxxoAwCm0mIkGDzdoKQcXsDFQ%2Bj7q7S1wA%2Fdgf14cwOmJ3h9unXTzi9jqgOI0h41%2FETsGQcdfiRQgdrycj38alHSa%2BHtvV2FfLgyzXNzzCmoiwNJs9Rkzu9cJlDMgP73ePArLPrQ0Yl48G7xFLCIrJFGAKkn%2Fa39X3gGiRG0P0rOGruJ8yu0yAJAMWE1qupKj7%2FMtn&X-Amz-Signature=08fb70f56ef384e4c555af26e4e517dd5538c22b74370035ca4223ea0d7bd1b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







