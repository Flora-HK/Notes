# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQLZBD6Y%2F20261109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261109T091441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIAeYxFFGyJrwQ0JYr%2FHo0Bci%2Ber5LES0NrgU3duhl%2FeyAiAO514bG9WarUUrSqFfAtQCmWY%2FTY6hngGyWYUa2zms5ir%2FAwghEAAaDDYzNzQyMzE4MzgwNSIMbbkKyR468SQEl7GXKtwDGtnwdIDo%2FlLaNqAIF85I3baJ0rCEsMBg0yIn8ZusMCfxba2Ip9mTJIQe9S9Fx24%2BcIeJvVmmE7pmIdN2eLc6pBbJvVG5Mnb2zox2QA40tJMJFCQFgh3hi786xgOx%2FX1Iyc2c6Go9CovLkvHrWDSyB7KAr1%2B%2BHAVorGF12G%2FDm6s%2F9QGATeOaCgjWpKuosPnZrc%2Fcek303kYsvOJVNnv84TwKi3RHauuvE1FkMA6oM4WXN%2BZrbY%2B69WhKO4%2FqO8KH7YLnaMVk0YLlRzqOIISZMYDXhW%2FguNe0I7FvF%2FSGJ0nsX%2FFD4SKS%2Bg4HEayfBrwkPjSrIx%2B3JQWWjBFEgyBLQ9UHwxtYpLSW0Vtgc34CyI3A%2FrFRb88oa%2FaoqAzzldez9cpYoZhHzpXRXzwXo5BJrmplHvEJrm1%2Fbcl83HxEiHE8%2BOsS2aO211kWQDd%2B5svvqO1PqsP42Yl3MTTei3mPxdUB%2FFDzKyQZRiysAkrJ92cpZ577M5H%2FmEI4yiS1aGLL%2BxmXDw72bs7miXM2FyKhTHmAXZb6OQCtLfyLfoqZbNn6BI4yIh%2BvVBeezP801cDAkMMAXrce6%2B8JIemErD2Et2virr1ESRGp7S85%2BPb2FBfCvWdr8Hf5xt8Eoccwi4bG1wY6pgHnVeRYX%2Fjt%2BwWBp12tAdOd5BEXJ4bXLdQR3YWmwXuE3Cx4PMuUH0ahZDdDd0FcOKFQsFfqfM26aJifatvrBT%2BIGWIoReC6QasL8EzVmcip5AJ86muWqfiyfU7LJb8g8Hk7zvE4uABmwbnphNxauueuaqjVSV3G2JKjX4a256wq9yC8hTrSZ%2Fa0SWhNHvJZIIPCC2H2EQ8aku5csm6KI5zNBN2uowiy&X-Amz-Signature=48f507c5fe3790231c22fc5f99a37d7950ff174f403fbd0c45fbff9b59076488&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







