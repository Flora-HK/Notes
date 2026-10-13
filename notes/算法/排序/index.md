# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XHRXXCL%2F20261013%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261013T090135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCEzJrZ8bux2mVTM99f8Myc3BqXEQnS2kYgQh2ILRzg8gIhAMI5%2FKjqNVkDm2z5HnUcoTXGhH9HtMqaEui5jGH%2B7BdUKogECJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxsL5DhVu0xtD7sEKwq3AMiBGKNfx7NvzuRfoBnxg%2BPQdJYDSCR0iX87oqndZ8lQVYaXOWwXEnEPusQH9uMZTaj1PPKFfpaoNn9rkcLV2YlYZTDdjAyRjuk%2FoWVgswcUfba%2FNA4cUFO0lehCIAsElClg5JFGKIkzmaiJxIrmz8c8Q3iUEv5TB%2FM1H2SiWCZjziFFE2dxbFlh9iGvWHJQ6dtcmajPlq5LGE2Gkh0d3ELR8Su5rYZ4KNq%2FdQJ7AO7U%2FleCSnvm04fAEQYiYQoKjdStIKX19HEeOZ8gOVDQIfbnIf0JtNWejZXB64yjue1E3T5ZBaMPc7pSr2YhfeXpHQzJEhQ%2F3tLesBtkYwhH%2FFwcPtVU4EoTUzvBMldVQIbortzI7jbMXnPiRJEd9BHiZEw5SSYG8AuN0mfDTQ14yu7mQtx%2BqSJ5KiXExw0VHCzhYIy4WO4ul3KysNvbKynP9V7Rtp7cy4tMm1Rf8ETl%2FvYHY35Xgt0zbBdSShklXT%2BdmHr4ZRDwoFey1izZdS%2Bg0SrE2jz6on8HB9ddL%2B91e4mRZZizImjRg1d22TlioZHsRMBGd2q33ccN6Idsy62Gsi0Edw6P4XSSTpS%2F6Y9SJ2U4JExYxq65lvGXxRBls1Q8UdrIIdVkA2n6i52GjCotLfWBjqkAXTra7QmsinmIqQsBvUzu%2FezkLzb9xuiUHpeNsB2HcYt%2BeW34h8oJN9ryyt46tT%2FsmvSwscom06rydOC1JKhE6P%2BhOTQgM70qPWq83FwjhCfXWQw8XgwfADK29eCb24L1S2KimnSFkUeRoEFkDL4JW1Yatvl03LwUwFKNsBC3ytXUfJy2Lelb6FzYazKOEp0vH1ZBhd954s7oP8x3%2Bulet4pxNY%2B&X-Amz-Signature=e5dd7ec35d376063f2f7e2a5134bebf2c44de94f8e0225758c062caff9f85b7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







