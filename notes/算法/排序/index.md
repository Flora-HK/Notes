# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB243CIV%2F20261128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261128T095125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQDcsv5zSIIEC2OfN682rIooOSms%2BiqeJnTahbiv28jO3QIgR3E0xhjHHxKEAwTDh6qRlTIAffXQ0XUWEjY9DGmlkfIqiAQI6P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBRLQx8qBZZBLhh%2FbCrcA5G2%2B1slUSgO2T1sM3b7mrY%2B%2BJ77slcLWu0rDTTAsT1tnGxszPrbPHZlKh4vpR8tIHIp2Bo69vfaGiZ%2BNkDOe7%2FmotqbeS65WhuupwDJitZ9EZXgFB3PCYwrTYpyQPioj5%2Bo4nIxcC9LFRHy8aGfCPgNH8io03xZs0hP8pYrITKZ3Vj63R7%2B0XN5sIq%2B0T3x%2F6apOKcl8kipfqRrocgA6yMrhJ3KC%2ByUVFibpwK%2BHpObipLUT5Rcaso9e7JWwzhtez7PrtTjDScDrpLzIeer0MjL6tavoIVtvs5wXGVrhXJ1kDooSkIg51NuZy4W0X2JamkxxDH%2Bj8g7HdIMCOzeFmH4pgVsCr1bPVewBf88qXm%2FOYFRs9I4lpBzakUpb8uZalbVRlcUX%2FwfgpJ4Lr64C2nnWv%2FLV9dZ0vqVnHQQYTlNhulCTvMfJ0npnDLD6cef4MYly7isQ6Gy7LbjQXf0fWaKOIZRhx2SqbA%2FAzCRZEEkXA9thLNIWpbK8bMxlNoAo3%2F14E2W%2Fu88ejbKtpxMoV7axunwevXrK%2Fkpm6jtJkDw84H%2F2APL1FFsuzIQJyvSyb0wfLeRfJF%2FRbd61WlgFNt7FSV5sc13XdQ2TqFxMvRzbXTEmjFPrOyliPd5MM2LqtgGOqUB6BqQq2OKUOFPomDDBLuwXmzFTvZQjvIOhvquS5o9r%2FglJWDNUvkuQ%2Bgw5SU97OU54ecfctMt0FuF3Z6KKEhite6cOT71SJpI%2BuuovR0omfX%2BC3BtU0RkkF7VffupVo2HYki0K0R8RI368Go%2BtEmxRjrY8LLLz7xh83HtIKNi8%2FHXNEovs%2BQy8t%2FfNhbWm4QR9p6uB%2B%2FyhVblavHRHVNiJ3AYQG%2Bs&X-Amz-Signature=732f3a88604e3cd4246ef148277db6130d87902a394108e9f3e677ab68cbdb61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







