# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDKSAYKX%2F20261107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261107T082436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCGbkgL2Lu%2FlFMRr1MiLKH0vXDqIgyiiAxvHwFcV7X7mwIgM2kf%2B4p7OeojSWSV%2BDyipWGnlAzwmYz3uxwAydjhXtkqiAQI7v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNRHF98QEbTTDa6OmircAxNdlgo6h0BtQCQh%2Fn43h%2BvAUJ9etGIbX2ajLlgj1MrnjLVbPGsIEwr%2BcecBpeBCP0dB7i4CdS2ffMWgzpyE3RCpElY9%2FLOweiUdlUuavC8Ij4Juw8hO29oOsyVYrPq01MLjCihjZtLpqYKJTXVxyf3gROAunJe82whMsvJywwPK5LQpCDHE23aiCsfJW6qrtJMBh4lf9iWA9Ih1awW2UMGelMcejw5wU8WzI7Nw21vQhi9ncd8Lbaq0Tpvu9ObPiZrTpOPtIxilbqdQsEOpqyWvyDsIyQcg3Vo%2FXbMRAp6iucmPl5d%2F8pC6OGHu9qQ4T2HLUm%2B%2FpltANtYZ7Y0TVlSCXWQO%2F8hQUWZFwx8atNqpL2On26WSTsvqYtlSwoeZVpCX6lahERUU3zA0q18vR410BwN57iZtQ3zxOsZg4s9bTGUZyKVlPvMsJdTv%2FdV6rG1fJfvWBECxS03HzVy0fKpXXi6oPfb7%2BxNOEocwg8ZrbNFXjPS0Raxo%2Bd5F7etATk6PNgxJhT2sPyh8jDxQHePNfWwpu6nSsrniGv3znF%2BHuWAfReJVrNEPQqpe7ng1Qqw%2FM3x%2BNmJfMEX9o7zsJXBaaZfMCwTCRSuzG9ZxHW5MCrvT6JMilhyn4ZR5MNntutcGOqUBunHEvibFS2yZVh4rWpdORlMYAD2zZusQY6Pxk9WkQkjTDvjhDdaW1hPSMlLFTIv%2F%2B3294ZYTjOuQy2Nt6io4c%2FFds10TLmtajX4B0cSQvLgq%2FYF9R1iKj6%2BF5RmepgxBaBWBreY014h6ZYI6ldmC%2BB%2FgsFJ8Vg2C02ZzocezW8wsg7%2BDs0NSMqllo5WDY8DkK50syUYf7H2Z6Ju61uezI3GDI3mJ&X-Amz-Signature=4e9aac7a0ee414fc7c7b0f83864c65d3f4910ef4de77321cad5369296e917451&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







