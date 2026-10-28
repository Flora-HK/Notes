# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662V5DYJ2M%2F20261028%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261028T075801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDUaCXVzLXdlc3QtMiJGMEQCIH9pWimNmlCf9lo5p%2Bb80104CaLK2dBR1NFJgCfSq8caAiBTDnCVQXFKdiZ6rqvcv0lSD%2FNi%2B5ZQyw%2FAKI8WsnjOMCqIBAj%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFztZLEPDK10rjx9vKtwDd3m37n2oU41dVBfigeKjlJBXqFjDgLyJkKVxa%2FfsxI7YpszpLyX2pR0xf0Yqpujrjv%2Fj0tAc23t2JvNMaIXKcoU5aa19FS7w1%2BEbE%2FFLpMz0gHtFEBvhde5uGS4NgAQ8dBf8JBlSjnuS78OlV5tE92lic3nV9VE98uuQs5UOqh34dj2dd1%2Flnqv%2Be%2FjkSko5MEnO%2BWO%2Fq%2FbxdJGkJ6NAY01sQEL6umIJe453RXCWfIvCJP8UI%2Ft%2BBVgig8msXXkhjRs9roWKBuoAyVYOnDl2UY9eIfqS5COk9hylH4GZ3tNE7DbHncegC1uffd%2F8N%2B0ZwMHaYaz2JmfrqdZTZyGyPtbkixZ1jzy%2FUvtQddNO9qU3Sn%2FcPKFFyG3rYwAPhrvYKSCqQpZqtJfw0Ik5XIRGBgo4Omzq0FLH7LMpInBWes%2FTwlAMW5gAy6J8m0fCRwimK07remtHZX%2FAGeU4dvkZcIEIvFCHzKwAb7JYqZy0fITrgQFAL%2Fss1gWI4woig26u%2FCNOobkyNNPEZEwDpExifdj4mTCCust0dgaypJjcj74Wg5QNwvng6b1sY4vzXlFYL6J69R7czdnskniUSlZRz3u%2F6XniYS9jXfUK%2FZSPgEf8NSIGRbb2GyMaZocwgomG1wY6pgGEKVUOn3A8emCYg1JvW0sgaru1upjMYdHnIayAaLNaQkFPP5kVvInDoD0DnwhdYwVQpzO7bbN1kW3Uvw8mWF8R77RX3mfy25RwCyZVJhRsYyLbGYUucUypWvXVa8bICA4U5ZVrZ7CkYGHJA83fo3zGApBwJDvYaz5ZI0Jnezgh5iXY8OHnrxxfPsqoxkCoZv1UKHZQcW%2BLukAUb%2BHqz7OldGhIffWC&X-Amz-Signature=51a2db25357c5571bcb805da847e11f146a3e75e553025926158b8a3ce40ee12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







