# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TW43BO7X%2F20261002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261002T075914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDd6U6sxL8g4a40%2BwJjfuxxJlOp45cSqfEdHm0HzQgueAiEAw%2BF6DVUvTKfdWNYu1gcp%2BhT7jDsGTO4D61D23YrtoLcqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIeXN4k9dvZ%2Bw6wpoSrcAxEOXVpwRm1NcrTvd2jBF7iJWNydt0GsEXsE7I2JPh8pfmkXYVtDRDL%2F2eytqxEF354SlDKXllgukx4JgdThABA%2B0HW0r5xio0qJzatTaNDpHAdHW3lWAsB%2FQd%2FqQA8SmWKBbmo%2FS3Sa85C3%2BX0%2FlVkW8f4oSbn6xhilpPlax8tDfLfwlnZxbwqFqZjesEc86PtAtltdtXoFjUDm66lw2GRnfWtnjMCb3nmEWgoOpcyUwMtz8DXUhPS3Gx2kCxrdWvUz3IXRfiQ6HFT%2BFg9I1mYUh%2BS3AAkanxRU%2BHVediVIkV9NxZgpc2jXufHlZdKoJpVaa0s2Sl3Uwc6rbY58T1OLA4YD7IhICbIRfWRbduCJ6eQJqhVOeYK4MtOepAvLh3l4NzVFF9oY72BJR7xBNX5mf%2BYuU52BpXPJUMjGCVvfom%2FvyzSRTjEh56R2I6QVrCPYzSK0h2xgGyt4iaeBVl6hyARL1Fyj2uYnKrisHg4szV47NNZlwJRq%2BEivqU%2Fo5pu5%2F%2BVJOiU3OXMYn9PPodZEbtSVvRmPMCSavBihAsN1vjTaGPmYk%2Bw3VsxNo5M4yaLl26e7XjfaG%2B9jK%2FCpYLIlJ1r2c8fCeLkQULT7v4vOZtheOsqYP2NcOXiLMIfy%2FNUGOqUBeBD1xY6pg0oJWfiSIVT24CO89a%2B5n8Qn9QasmNK0MnPCRBhmzEdUC6wsahgidnhe9P8mhDRs4O74ZbFxkC0NvxdGGcgvZQv2PQjfUgiNJxpPTEIrE6QPZfvoUmC7eUvWsYFoLEdOQmPmqQiCbNzWxPx0y88dObus%2BBYApb1iUWXE8GHJZp47Ybks7CF9qWcr810QrQ%2FKeFWWtp4QH64qkAHhZN1r&X-Amz-Signature=b4e3886ae993c144fd6e46072f128feaefa7a17beace97780121517e82b668a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







