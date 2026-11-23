# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZHFJCZL%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T102204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCEw8uBGw%2BqCSbDVueTucjQi6%2Btfiy8hMwXQPodU1hkXQIhAKcTT%2FrHe%2FpfJFrd557mN6uv4C1znWeKz%2Bp6I3r9TvTrKv8DCHIQABoMNjM3NDIzMTgzODA1IgwzIFOM7wHWC%2BBMUFQq3AOh37mXocOAakY0wBeIsvZXzuOEQAQRhhYtB71pY8x2c6L4QKgs0ff48%2F0mpugIc8cvrnXvv7UNAT12V93u8ftPtkJqLp6rN1wFtm0VYb4LaD08i0BBjmgegJD%2FWF%2FCz2GP76z%2FH2TTPhnh6V72jZILJI21Eij5lALV3edUmTy%2FNcs3ngc6MvCIAlIYf3I0oum50rrpIXFRiGHHGJfonpRs7aPSoVlGjSFZUqKFLHgQif6sw5YY98w2AkhYF9spiv%2FokbZjirZFz02s%2FYQj%2Bs0uWlWxOxel68Fel6ssYNITonPbeUIv0WV%2B2hB%2FQ5q1dQEHK8zJXLYGHnDqBM1TRAvzyj65oPAtTz%2F9KbqzFdzPVGu15DP%2FHfYQ%2FVSCElSs%2Bko3PVwxvJYMu418WLoLL4ZAwqKVm2XrcxedTW2bKE0fpGI5s%2Fhe0SpebQGOoHpUYKVhn5LCY%2BIyFNMdoJqo54arso7WektiRxH8zjqDdS0rY%2BArlU8MJiruPGFN0hi2%2BLN%2FaZDz2calcb3A0QsMF9jHpcVepO9A53EbrOETayuR58gEE8W98E0YhbfXDwu6I%2FmminmfOVtPOCy7giRHO2BN0ZRju5ckK9ExfbbX5I4J3LnRP%2FWRy9paujZdLDCah5DYBjqkAVmSuzR94R910hQJhAeEA64WbRzW4OKatWBtFhhwe%2FQeAYvQnd77rj2u5KVnhyjrBR%2FHMR6XamNUztKbVAvD46%2BzCXut%2Be4ekGBAJmoDuyEnsaOJ4wVd8z8r%2BDWGYUS8AAFcByWWKKh0b8SkViDnnGBtiVbGIOEsR4zHjI8zyXDV%2BfeGr%2F%2FcPxsdMSrSN5hVkSF9UKKvOBRkw%2B5YVPEPGrHNN3pi&X-Amz-Signature=ec0635d8965d685df9a8cac525b6f686ff8778d70fdf49fd05fa69ee906f9538&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







