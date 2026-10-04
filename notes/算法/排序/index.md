# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MEPDFI3%2F20261004%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261004T074929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtNtJ5gDPjleugTgiilkfuPoMHcqfq1iFuL3u3ZFQc5AIgFhxdCaHITRR6oSWVWfAxZxF517uvgdYAjD%2FJsQcTjsAqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjVEPC6Tn9WVqOtdSrcA0SJ64kKA7VtDwsntVM%2F9WztISbs9N%2BXYb%2FiqSzgdcaYm%2FdlmzSKg3Stq3vKRbBXFYbqV5iPF4vf80B1%2B1s6F5yC3jIae0vMQCCy9u68xbAu4pHISXYxT3t%2Fk8KY13KurJwEBVygEygdO49DzeuP8zas2UTaLqokMf8JVQM%2BqBK%2F%2Ba5tKCeVnzo7Ylbgn4mkPCvFg%2FQQ5slFhoUwhrMDfBgCLa2KUVq0NkpontleOWdEzdrZ7cM6HaOFRFQ9BKYqMRjAPDRCyjPL7KWBHZMd9%2B%2Bcd%2FhbIxVryWDImLVypYaL9C4Eqe2AmlHewE9Me9%2BqBQ4eWImhWUI6DlYoOR%2B4jPBbv6%2Bb6f0sPD0OqR8P7Wfi53h%2BGF%2F6ZwrCLM4lNNOdmmbuo6%2FsEQePwHN7YhCqvOmXt%2BNBB4ezkD7moqwIO9NoXbwTI8Ac9dUZTDqSGbaj%2FDrG%2Bev2S7nZeistT6SDBXx8pZOfKHWiZ%2Bxs5InCV49NwepHmZ8srHwXaqNiChiPfH%2BTyJH9pDRGI4kxB6X5FWscKWuFsTl5jm1CTHJn8SbsM1eGB6p25dVhQFUvdjF3%2BR36kNwJjTw9ckNv%2Bb2TtyihdMw8JIWo2iidy1GxrsmcGNdHn5kzd8HYn27rMKPah9YGOqUBk%2Fu3wJIJu1H9FQkhtfSOOjNDKsoTsuvpBL%2FyaOvzrRTrbVxA8i6M%2FG8I%2B7R9n5tFPfaNu0TEWIp%2B7KULYTEGtB0h7OnMxrUhBFM6UYCRqIQ8nwrYkFUeZDAr4Mlb8i6%2FB02NjwOGYnoD8pa76iyb7uRt18pltZZPP5WXH0OJswxG%2ByEUGIss33zm%2Fz9s%2FQrERCqKGmhHSAUnHMU52KFBC3QsvdvS&X-Amz-Signature=bdbb305f8f43fa81b942711c4863077b8d9884e023fe7237ce44593556fc1ac4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







