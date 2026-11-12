# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIJGFUVO%2F20261112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261112T092148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFx%2F5kOp0vJZgZ3LxAPLhg4nE9BVDeeR5lUqE8c3Dzd3AiEAmXZgJcTBslaE0oSF1aJFpBYmNQDteKFng4DEODRE2FMq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBiA3t7W%2BmNR2Q4GyCrcA5RIHVDhxpVvNPOCEa9T35KA6aVDalRGoVcE%2FWj%2BCc5d3TL68f0kcHjRj6w9uL3RoVodSdg2tKdahzE0cEVyEypPs%2BowfOAZ2sGkVR0Puz0t5tWIMrfAF2kGm4qkkOdMWwhkMNHGk6in4N9wsiX1uWNBKQ1Of8uRcceIXBakFbpUqyEEtYowfmRXjRlhV6tHoaNrjiADvmnEGVyoFf0aUAjS%2B2Z56cnf7nzL8lWZ4VNIks8UTOhf8Cq3D7SAKKwkaQN5dvbGOO8bpY91CyzRU4ocVyIQlMMd0ptgOywaXyoel%2FwFYtyraiCv2z5jJWhQ1v%2FM0OwZKKUdcd%2FmcFINCmih75pG6Zv0%2Bm0ruIourM5cIB4nggqbXSeTCfuFnfRu%2BkS2by8go%2FWMJQnZ%2BBYydX1QOfd2RJoUVdBFJOc9Q8SdUs6fq1ZUz9PBtyFS18VNoyJDPvDBxkyoHsz9NsMHW15oNrSzNUquSgoyoTnakZRZFFRyeDmYFzsce0r7e3YNcRbx1ZBfJOEYi9JQFEjrdzU1g2W0Z0IlxXM9KxwD0ISCaTdW7hyZmuuNWEmvSe%2BeYz8tbHxtIkvw3f9bME6B3NEKD7b%2BWlSoeo%2B67P4iYXbcQOfQGzTMmVT5rwUrMKn61dcGOqUBYEchLKvk2AZHp0ISg00OzAGloQKJa2Riq6cZvREsS7RKyHeDsr2o7iqUpnYpg87i09pl8uii0L93WOddZOu8Xo6KthytIJu%2FMoLVQAZKRedvFaxSrZIXSg6IVXYpx9yWG2wJqCIkdWzhDLRN25dSKMS7E7V6xnwVUZb5VthGGZzWES%2FtCpdsuWQB8m6MLEqpGU7EfD1MvFfexfGlc%2Bsn6AuQ2hgC&X-Amz-Signature=7287129779eaacb1763bca6d2d55fe394ed6bb6228c221ec55722d4801399d07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







