# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWHYEZWN%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T072302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTKK6COsZuJYwOUcfCuZ20aHQbL5eTAy7oqCYsZ0S5DwIhAPnSedidb93DeI1qooxMRV6Q6X5nFRkPO28OS43%2F8Du%2BKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGxNxPxlajZXkGtLoq3ANvPhXW2lPBFK5AjDW1Ih9InQ1tLkdpXSNI8kewkwIf6cICGkBmUcRGrq%2BcMuJmuLgsy%2FT%2Fa9MbmgQ8E1mT7Nl42OH5Nro0abX7AWFn8o7t%2FBelpVUAOaqNyUQYc%2BO4RzTx3AV%2FwaTjiDsIgfiPHIEcl301bzzLCb5%2Fxlp4vb6Nzgc%2B3wZY61d80%2FEORKv9k4WcxBmPPvU7YE11Vbz3v1KxiRGDb1T1eF%2FSGa8NDyjSoClh9oa9GdZBRLjsUGzUTonQGWZJUXDno1kiYiahANljt79nbyXF005i2vUm3MkyDO1rbwBhmSzJvkgoXXmUuMAKHv2QA6%2BXhvqnUHxSjHxkfmD4%2FbWB1XTO6pB8MKaUzeYKNruzYYuEvSLhrZD%2BbT0F6UiKF%2B7%2FVZXJMzXCJQzNsYhUeXPZAvkV11HN3oYSwyPhJWNzcoXg83%2F%2F8YDIVuaqBjjjnIqaVPZcb5XwN6N%2BuFnNaB5bOxa%2FlN%2FkRFVYpHTar13TFcV4TjTWoKNgyJ63WHD%2Bv6mQViy8WyQRutKdiWpcrZ2K7wnnShUVj0kZ5sssqt6s7%2FPel7fG98t4UefkTaLl%2BGxHy4NXM%2FgL6Fhd76yzg3wD1ibInOA3EWwzzVd1OetQuQOAqgGeRTC4wMjVBjqkAYvMAQR2JD%2BZA4su9yVUT%2FKBFieJ3b0KkPirfZlmv3hWzKM%2BaxQQwmZAV62OvftV2C6l46xjGtfyHL74cs9p1aMmiaktKeQhQQzhQijDtD3KLYwPdmXVy1UfsnJHmt8DQBhgmSPN4gZ4RyYNfAeNy59uLtDvyoSpdI1Gc2QQKDZLajx3Kb4wFiVcSrIZiQ0kDeU6OquKc4gUd0R%2FDdUwOJYhzKXw&X-Amz-Signature=ef993ee012753ccb7b1546e58a47225be61285743c22eb4a5311379125a49117&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







