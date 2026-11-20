# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5BCDX7S%2F20261120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261120T094412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIHDMpr23MPLSdIn9jlXymxIfQw0yfRuDAZtoEF7P41YOAiAXZnSjLJ2vqVNN23nfD1H1rlrbESXdLXSuTlOKm9Gvzir%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMgxf%2BbTYn7NibBsQpKtwDPcfl2ClYG0BqXAkutxGC%2BpHeDzmmVollggQPmFtj%2FIMTeQZswivplE7e6%2B4ZETSDw%2Fdfz3Pjwu3OYDxfbKg6vU256VSpvEL5sOWsIYO8Ef%2FyA6NJmg5AsALjZpE3J%2FHiOj3ukC3QPvnKAH9FXUXE8s%2BgHLqeqpBSyauVdcMne8PFOsnzaE6%2Bu8j%2FRfXopfv4BT8neP34xfAxWQhCv9Wpm19Rk8PF%2Br8mZ9%2B9y4eWWMJZr33WLcw0lObsXj3t68rzbaZHrKMmrGEhUbvXjDf%2FHrNxCF4tzvrGki4x%2FtycrnFYFfRrJEWF9x2CMH7VUTKcTeMVFx40MiZ8IgrazGtclOQlyZfrJwDGcxpQ7kKZkgWVOSE13EfOuELZ0lJbAqhVIX5UytmDxLPuRa1Tay2Cjo88So8lZ3dfs3xcjVmPOvSdvIXZ3mNxkFYnUhF5943I23Of%2FRkSaRy2KMUctdxwU28gb4ONjuY%2B7HYerk154sxjo9kf87mZE3k1IlnGnqSCiWg0N1G1GR0zIBrVBZYGrn9Dgm5Vho0zBtRrtU8vUS7xcpbKx9sQi7HvtHHuUH4JLx64xaEU%2BDB3DgossHf9T9WyXewBDkmL7EEQzSSBll1DNXiW%2BQD8C65KJYsw8YyA2AY6pgGcZAviPYYJynMRMVPaRwxVDBNK3WlNSVV1yyQC9sc7rOnVjxSlCm7m3cKnJwlWldxHBR5L5M6j9ms3tMD9yztMi7b8Lh87Ih6uCphzs7e1OPd8RZx%2FvMFxvnarkcsUCVjdMPutxkMjLEK2P%2FTnnkbuXbx3u7inJV4d6rB4cKzTI6twkMJnD%2BYUWqc6Uj11FwvaxJQVsgyy%2FLlL2gVVyDtkkKTAbYXr&X-Amz-Signature=94754ba674095389cca8a69f770b3f495daed583c2646717e04021c25fdee3d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







