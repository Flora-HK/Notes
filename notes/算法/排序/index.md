# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666O3GMU54%2F20261122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261122T092553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDL6%2BQjUn92XL%2Bg%2BLSDdsp3hOye2SMc%2FeVRLcsa0O4e6QIga99nEwu1AzzBu6I1X5wGe9fafeNXtfmbSJhNj9o1GrAq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDMPyS%2FsqZZlvmno9uyrcA2nI4pAeMuX3z0bq9wzIvqqwXw01tVyEQG7n7iQ%2Fr%2FDvwzNukczg6y4eMzxZ7wcz9Rr7VVkQU1flBJ87hTM%2FJeduYG5aA0zWCoc5Zp6gh4gtPbveTzdpFd6xUrGWHp5dfYUrAZtUyGSTuvwUFhFBRDj4vxNePPLC9PvQAB1buZZuYHFjjYJ8QK6HzA95VLN96LoFNEgBzHvBwM7eZgedZOy%2F2uh9ui8bxNgPxsrGBQqatu4Gq3E4NGUtKxTqCS1zwbzQEKaAw6iptJ2xlrW2EDi%2F5FM3hmI5aZI81mgGd8Qi8jLtG486yO3Xc8%2FLj7aOuU2iM%2BvneNQIsKWg%2FWos%2Fxlflf2%2B3rL%2BGSwlmM10QuBsoAOB1JyCejCY%2FF%2B2E65ISOrWuMlUlax%2FFCEV5bHEL4rpTOTCiiaPnT%2BNXLcGFqvDxlFK7H9oOTFxP56BVTpXSWc42%2FyRzG2i17OgwvV71qzk%2B0f%2FFslDotVOPQUGEH6zs7ldhlgIFvjdSquYIaGUSlKnQh1Y3IoxEaAlopoHswtjYKUP2aYvFv7EXZhPExkExxyw6qaAQxDHzUtUUJ6%2F43DGbePcp1Hfjxb8NHRH93%2FAdQ1GpjLEGAWxDbrP03q%2F74xjNi09gtkkxCKjMObKitgGOqUBgAyFhDY7mduo%2F%2FoWReHxv7lrjcKeTLICitNOQLKhji9TVMqErLXgJgxTgdgn8no%2FCUu5LuWFpRXE439Bg%2FrJA4NKptRlTcBK07zes3uHtg7QRHczo5grlGeDwbLFN4e0X1wkSeKIvuH0iG22VnSpfUrh5PgT7ooQa7gM6vgrNJAaEaqU6n2BklxrzoMi7HukNghi52Xap3mqrOgKIuYSQfDOiMgZ&X-Amz-Signature=1e6dceb8e611417f724b82810be905e9c02d5688b86ec58a5eddcd45bdcdb687&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







