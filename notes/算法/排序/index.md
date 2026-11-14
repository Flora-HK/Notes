# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTHO4VAO%2F20261114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261114T083944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1EAYrp5yBzs9z1yVoStW%2Fod6GGIIqwTsaGa7E4Ua3YwIgeQ30GMe7I1s4y%2FrhY2QQihZ3NyBdRniNnOIhsWBhUuUqiAQImP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKxtkaKfrTCUDupu0CrcA4yepfzFVhRg48rCPJmZwSHASDSzB6lFej0OUFFKHsFXkkatwahR1OcPpAHd8nVM8qG0Ch3ZUtG9TfKrAr1crOdX74fFolY8MW%2FJg2HldnA8788CeqyCXw%2Fck6l15XJoriUMURY4zmfVAylFCYNSKgqxeJFnkK1mgI46EUIbzFNu52yFbhcSvIJP2FV7IEIgbtX%2B3S1ibSbEy2zQX3sBSYdI5U00rYsRrQaMIK1kuYdqwhv8nZyCcWfPVTRYMJAdk%2FqfaIzq0AOzPZiuCVPQv0rCnn99pn%2FqjiUHVAm7V4ZjliAOZJ9bDRhx86LI3ugfyrdZNLJFJe%2FcfOI0cEIAif0PW8xc9r8Y4nyTZUFhU9ySQpsAwEde1OQsGSbYP4rsjPQiF7ogbXqbeN%2Be1f7yd8MhUCyYKz3s5R5MmB2aTeX9Oz78lgQ0gWMr4fqic%2Fp1YuFsEI7dzuyAliweCIGTSGRH4rA%2BiJDSWi6%2Bo2oomPM0k9sizUUY0pwqvjsKJTz%2B2j5WgJhockrPNIOabQRrjtbQK014bPX%2Bmua2QyhFrlgIORDtBCHAX5fq0OUNeBBZsKL5Ij9IaslisEh3ATgSu27UWhyg7aAreMtXnTAKypM%2FrX2u1NDg%2Fv%2BUOvr%2BMLmc4NcGOqUBBBEJJ51ell3RYf6vx9%2B22ZW2qBOH4RdlLpRV79JlagCKbrB1W9MUPbPteyB%2Bo0tcXdYqsL%2BO7qheMpD5%2B7yf7EHeZnkd6faPSDktPLk%2Bc%2FLDB3Ffb5%2FGTewMZCv6W84cnGEjZC%2FeXAzJG4FujcTLN30ODwmDGSp%2B762cMiWHUbVRGlgeWzmrcuFUSA5vhAguuO9DyuJ9pOlPv586KN7gTH1vvlRz&X-Amz-Signature=3aa9e6682b75f49df8cf6f79531a6f9bc664119f73e01bc07668e354b9b33c45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







