# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655KKLHS3%2F20260924%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260924T071655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQDxViXKaxp2h6YV%2BSWWuzJskASABafqF9oxnglncq6uIAIgaFPbtYDkPrhAy%2FkhMD74LSlO6IOtMalio6jBgFJkXkEqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOXihr%2B4yeCEZ55AOCrcA3TcqP7w10I3LBm8%2FbBT5o7yGqj0hHrEx8AHv1gTlURf5sUKXHVFIfntIlZDoYpcRtQ9YNcqvWu6xscvsM7eAUUaPW2lzrrnlq3oUuLrDxidzsaGGBbHgd%2B56yr6BUP0i7FGnBiXhwJd9W%2BSYnQCziGfeOZNmDWBCpgZZxDjXPrGRqNMClvsX6AtWNmFQmqEZ9Kw9Zuqlz8oAkbWAXKq3WdgIGX4%2F7WfS%2FW2eq%2B3sJMTyIrusLYZGcIPGTWP8dEGy0MP2mPPKK7rZ7Ai%2FJSH11AsgR7T05C3O5DsBkWi2WQEWmBdR5FeZZTPT2O6SKWWmFGz%2BppnvwiZy51UB5ZDaAJD%2Frx%2B9o4f5aYMqjAxpO%2BQwBJUmwJI%2FfiI1uigy0WDNVkX60yi4WzvrpalGgM4At3QOc7%2BYvYQQpGlCQ1%2FADcw8gWSm%2B%2FDGvkcumPfHBkwhELhVmgXSPkPd7Prhd6NVzNyNiaspQsU0PhAAA6brNzKkBI%2FejSDcI7nrAHGVTvUKFWY05PZUjmRkv8tDoRFTukBdgjp%2FhyBwvt33NkQpu2NOPA3ssi2vqnpqvCX%2F4A%2B%2F%2Fsp1Io%2FwT9Y%2FiUHLVq3M0g73tL24r6UwQ4G65k6t4En8rGEaZay1oTqrrhVMMXY0tUGOqUB4iZZLCtZx8R7v2G5cOc6Yf0BKYcIifChqPhKHQOSbMB9zDx7%2B2WQCnp4EJhUid5XC8%2BNPcA9uRB5eVXWn18zvhEUFPJwOmrYiIv76Xbnnb6pcD%2F%2F1z1Akj5Aa1Vr2FubhKg9iJuvwMQf8e%2BbvKqUWCTiXxdM0XifIM7ZvbIwoCnBPBHuVnpjDxDxvJbjP9w1%2FyhQY%2BPgFkARe7BPLJoXlgScaFOU&X-Amz-Signature=bd515ee46fdc0f819fedf0b303bcbad3300e839be183403523fb1852d4413d55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







