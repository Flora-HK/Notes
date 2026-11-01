# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3ODZ4BM%2F20261101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261101T084755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDM7EWt%2F10s%2B%2FcUF7Zls3rrjAjB6euiBuPb7ZxvxyvXVwIhAMvWMxxymEEQ7TbJBNz%2B%2B3AnOMgn55koukymhLXJ4P5rKv8DCGEQABoMNjM3NDIzMTgzODA1Igz0crdomGfTfzcjjHgq3AMlQ6ftS76B9fTHqbTQcsoa7TFkZy%2BFAdTUZtrtwcc7%2B8Myqsm355LOVv4DDLq1lya9SSaKi3t9jcxAxYfJqfmPCxPcCUnwPkb21jcDPkiAgYJcQbMyjJyHg3dPPuxKzEAOrs3H3z7Hp8vSNymg%2BalNdKuEQ%2F6jTKThB1Pm5009%2B%2FphCxUm6QmArFq0NYSbkhCbc8TzGQtWXmptSb9q6Agu9mcud8EZP3PrQ0%2B7RChqV00vHU%2BV08980dbaBkXhkrpbil4IJTZGvcne8QzhVvBRyR89lO1v32YepAUV8QtMgcgttyROU0cK70Uf67Jw%2BqakmYjCitKjf0s5Gpv9EWRoqJEtcz4NCnXDXEEnBK6n2WFJB9I%2FAgLnf6sCRAG712ofEF7o%2B9HFbnTD7TXgWZMwBriICxtWiKsegkACaHJymvp6YFavupKaTPdI0FboCGWhsJg1zxvnXWMT%2F8qJL%2FdBfVKNqh%2BKgdwyfgYpeeA2FNbv8U7bC19b5g3bl49hMB7ldlPsTiE3peq%2FRgI6%2BCDI2SxWTrR8CAhkCKhmRSLqbrMXq8X%2BZykkFphl%2BX5PFdPfmR3Bmje3sG0XmYLaP%2BnIE18PBxds907ee31M1WMbA5%2BkAhhXYvX3IxuDcTDn3JvXBjqkAWGv7bTuny2n9AZw8b7K9yUNtmVrhlW%2BTEM%2F91f0o6u3zK23VMLe1XpWiY5o7El1A5cn2kADBrG4I9abogKQtWG5i4xTT7%2BXh%2Fpu7lZONCD59ltoOE1guTbS49tCUUpNRXHGl6AKsGoI6A%2FjZ86A9DsZ%2BdIKrwtn3dlSmtayPIqroyfB3ht%2FItLhx5%2BYAIB4NGmNE7aYxR10Tb%2B5C%2FfJLTFlSmIr&X-Amz-Signature=a1796f581d5d096f85baa4fb6ba6e5251cdd00cb6bdeaa3486658ebcc850150c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







