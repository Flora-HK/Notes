# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJDK72D3%2F20261125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261125T105518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTEuHHyNGdkYE1stQvtcL8gxwUR3yHXgySXgTxa1WrhwIhAMZktpmojR1%2B0nnROf48gnRI%2BLR1AwmIY%2BniZtxm%2B1xYKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy7rt0M1S4eZAi1GXAq3AP9qivWE25cNq48T6sNfK5bdPZqRxGq%2FTvAH1y7lop5AWaxuqYqKuPpn4Z2HWs4DlWWuA%2F%2B27Q0nlP5IhXklF7I98%2FTz1oRWjnMtUeqNTPTEmsY2%2BANvSZLMmfF4aORvdkiMaHkc6McbJwYDbZh3%2Fht1aVSdoqTM32wH8gLqSFpMWEB5B3W7aSbtfnxIaebefAcXW0dg4lUlEEZ3HIPHEzSVTLYQNhkX8d495dppBLgVbE3LANAMj1ZDmPS4ol33CX6WzcximPgFOP3HCMbwAJR3mJCuuQxQOY8T4YZGx6SrsrmJbepmn1ol4whmxLfNfjOQzXyPQQ1llVUbMELZcyFt3gdJDEzoOPRRqTn3ESUhoiseHawpI8fF%2F%2FlyngeTjq%2F2cMxFQP0doDSWT%2FwzCMmdBCKi52axfQHAfwFrusijEZwB4z2%2BNLF4ZYLuQ2FjpSMywvm1IdvZwKv5R5Eun0a32mj005hA8hhzQZibBKqUb%2FcHhoDfc0Hl8m9TrzHHO%2BMUJMsfFgsSwzraNd6yrTECotE1DhMkyFp5h6cxjkyZOh5zo02SYp%2Bh1aRH0E5ohNFYzeIYVm7yJq6mCaDh8ZLrUUvIiyaFmbH%2FRVe5NCr2YdC75AlRNTFN0gxxTCx15rYBjqkAe%2BkOIOh4NKeSQBjWyhYpDIbDFVYDWsFQBzDd2ZGjT7ZtcO1HT%2FkWPdm3GDmoXoquJgmWsYQ3g0ZAbDHcjL5wckeCMul%2FqV7apNphx7Xo3HI62%2B1bNzN5k65IV7OUKPWhZUI6%2BlaL3SSeCaAe6d4kFS2gcZYbQOpWP%2FQme%2BlfognlFrM2m68ZmztNm%2F3Idm2yA2hJBzwunLJaEmBfZB1YkVcgMpc&X-Amz-Signature=6c1c65534473e57fdd68f26ae2e0a8bbe5883c784cb254fc825a5a44e056ff77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







