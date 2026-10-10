# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664N62OW25%2F20261010%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261010T080919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDspeHXzIH8E%2Bs9WXZ3ZeRFFBu0hPBMlUHErGph2z4iTwIhAKcJFppJ2a96kCcL95vgouo4TtOjPIT1c1MOjvuX9casKv8DCE8QABoMNjM3NDIzMTgzODA1IgyAsdBLtqVnWfztPiEq3APr5VKpjaMauHYzMJ3vydEOxz%2F8dmALmcjXfMsmMu8%2FMNHta5NAE56uoopTKn3DL8uV7oI2qAYPmeAA6VJ4ppUXmqfjYIGtT3D%2FWsCJrVYhXF3C5%2Fl9bTrGLrwxCr3ZcbmZdlhvKXkDFmXHCMUIuJxmO%2BY%2BzFokIHVocRSAKmiAVnm8YfX0L20k7r%2FJoxsjsaBjrpyZPgJb2v%2BezfJ%2Fg%2F3C7USKiO%2B7O2Za8uJ7SnTggEbt5OFIk683P%2Bz2%2BciSooIArpu580o4zqlQQ63W%2BBxmTmFp31Tnw4VyR%2FKVKvUOIOnS5aP3DqgFmmS1sCQfZiyAYuPSiu6CZ5d9KzZrW%2FUyB%2FXj3M1846OZPKXgl13cy325t%2F7j6fItFq8P9LQXB7a0lzPBVRs5Lp1HwSYK6fo2YiZIZHxs0efZ7CVgtcTVsMg7Oj7feoAkqqNPv8ygDfasg3zM1ZQdDC1ELiXnovFYoHYGVZ%2BR4xSSis9ngXjD5zDmUazUgI5me8P4XmHxgCXPKee1b9RIRGASNEdRoPKR8XOz4wo9iz%2FvCiMM2sO67qrX4s4XMn2DXXG7JA81QEBExepbqZtd0rUFzUfvXgix%2FwWDeSXSkEuCPPLNgydZNu6Y%2FYBFKWiFP15SPTCYt6fWBjqkAUz1MxwCm3B%2BGywZTa38M3CQ9Sh8aIbHA%2FjYgBRKULqlH1i5XI0HOlIGTv5asbOQwdIvtvE7cDXrfAOKN0NVU38l%2FPUtlq0mYB%2FNTElVQokW2KEbeGUNaD0qH0UzQgT64IsoeE3ZQvDyTsKvVfPI2dXh55tM455yM2OPrXRXYbBMU35o1O231nVA4ieugdnEjQ7Kt2K4y9PAwmAY6yRtWINxH6g5&X-Amz-Signature=04c2a74883730024cf4e68179025334a3b595f04d19da098ebdce516be5ccae7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







