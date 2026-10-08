# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WUCW53V%2F20261008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261008T082855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIAUenq2m7SrrYnvV5n9%2BwTI22WJ88fyB%2B9Pl7OcdUJ%2BwAiEAjzLDFO%2BCoxLjrzH4gG173tG2uKnGC4ZzzJvnxv%2BERMoq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDEsd6Y6kntK5E0RVxCrcAyLI6eO7TZmfHAn4Q7UD7vjGz8b6RmGP6wDfZmE2ZZysKhq6Qom5%2FNuFKr0ibOfpvZypVDKmaQt45nDwvXwLKcHZw8y0VpAk4OTvmEsEwaMXbZM51W797gYu%2FdlPBpkZdp%2FPUlJCqYamkJ%2B0OBUIfe4UNTT7cuuub28CDjZOyB9LXBtOub2Y7%2FdQPWqQKjK%2BrJ2J%2Bt58Cg7svzU1YZbwOK9IKRCiBxgXw2j%2FEiDxr%2FpRgx6ZcqiXu7P9jrXnUv5H89PxJOwqT7fVSGj1EC%2Fic9pvKB%2F7dsNKr5bg8G3zA6Woxv8wqYMDy2yxPzVeYnbDxlq8Dc2mGtGWPF0Nbnd0WfrRdFhNsAT7n%2F1cRg1DJeqiPY7fF5KB4s%2BizBzzfOEjwdbH3rqB5cJbFJM6e%2BcWLlc%2Fg0y%2Fa1e2LA4DwY3d%2BqHlHfRzAlz7iqHEj7liAXzbz9l7rcIORQmD%2FLStEiq%2FT8Ej7tAhNTQsSmoKdUesutpnqnEnPxSa4Ea5Z3cg7FeFqosMrB14jZtPivQ3Kirtn4YyAUyg%2FgyEeyjtLI2xxv4D7CjISLTh%2Bop1O5nDBB7PDYyQZOqTQecLyu0HsiwGtAl3DULRACihoVn%2FwHkIqXtndNOLf5Fho1XngxwxMKaZndYGOqUBZcyzr%2FDBkctd66KSTnAJl%2FhbEQQvizWki65EDf5YCHiPbUwuwNxP6G5KjrDHJfUPWIBmvRW2RMptAlkgwHw%2BI0Yf%2Fy3iJzzES0vy%2F7cePOTm31Vj2if4oqPzCxl%2BVtFbk9ccTp5cDpkJqewOrQ3GBubs19gUQcMGI1yg59U5cBAt%2F9vOy%2BmTw59ofQC0CPZQ9Xi24hLbbQaRXpCnk0aqByKofFGY&X-Amz-Signature=698cd23e9893d0f38454f0536b6a19fecf09d9a34827e34e76ee520e8682125f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







