# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644ECH6W4%2F20261030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261030T080843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIDUV%2BnrgG8nhfF8JiBABlB%2Bfn0NwnHZ3mrr1M7OfEJl1AiAmoutMm2F5QqjYJUUNrPNtlHPmdTJ0fgtNfW7zikdG5ir%2FAwgwEAAaDDYzNzQyMzE4MzgwNSIMTuf1JJrnc2DxE0GQKtwDOlnC5qoQDbtb0IDkmbTGxR2OIa2BnPbydTOjWx47B48YwgKk%2B44dKDRGpb4NPjL%2Brv%2BzlZXrWxxm6xuA7zXJyvnYDSZZa%2BxX%2Fy1EaX41PCur0YWNEoTjXV6aI2lfub4JIzu6EH9nTq58Q9lNoQFxZGrvZKYxDd1Nhb39Vz6r9tFEpCa9sFcvelgBUwQnheSuKNI03xz%2FrcFI%2Fv%2BT0t3r9N7IJUjMCDc60RFn%2BlSNFVxzx4jexWOZ9xDYJRLGKhGDU%2FCCgBXXtze76tO9uqzXxyM1k3ttX%2FylagGgJzfGYnrngRAtX8ExkvNH%2B4%2BCiZIq8X0WOSZxuKm7Z%2BOqDLv3dmGxJ%2FK3D7jwZYzG3RcTQFuMmVXXIMZEO0%2BYNQlW5hW%2FmOjTDJtqFzsjZLKvyuxAT4CZlQAuEtvBSB4HLWdb%2Ba%2BtNRdrwLtsQ80nLIeiTj%2FHVFU4EecveuIfrJ1s7bxzlTa5cEwLeO2BOWFQi%2F7DzYRFexu7lS1HDOaVeI2b%2FnVAVPju0%2F9NihD46IvwpslwaAubI%2BqkCFjDkXpAvhizJ87tDi5juea8Uzd2zuHt2akh%2FQ0dEKOqNhtDOGTUvd2GHtiQgpysJF3tWtd1t28mY3uDyzl%2Fwbnekxwf7HEw8ZeR1wY6pgEltKdkzcfy0aDtDQDjLddBVReTSw4wf0n7eryfRSzBl9vuXYYcIG%2BYs7cn6GFfutWBa%2F5WpeH1lDwUo59H0fJ07z1mEDrX60HQrINV9cYzqJFlyIkeiHLuH13yUhs3KgjUb0cGZSpGUN0eikSgrcB9eSVIx125WIs2GDhQsYVM8oVU3wBnVMg22QwaKu0s78ZdLnzL89u7n2zXG9vJWnlUqYcCEuD0&X-Amz-Signature=128afc503d0530e0ef47c9428ee28a18122acb7b93fe773a6d83173795964676&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







