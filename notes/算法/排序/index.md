# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7TCFQCX%2F20261111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261111T085442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4TpYhQucwqppI%2BUaGPo%2BKX8YyaFt8aumBJmAyaq%2FfMAiAYAVpMtzerNBKB9Gqk904zLE%2BFU2uUjRyS8lJX2rmQMSr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMyOJSWYpJlkWPYfvjKtwDR4te5IFXrBuY9WfGD%2FqKJ7iuPVLYQ%2FSWt8fi%2B0uu2NI37Dt19ify%2BXbiGv8D%2B7%2BjCiEHNysbOQd65OYL0BF1IZAI547yYMJhy8KoliFVtcfBUQQmC7PYltgoWs3gvO44BY1FZQpZNeZNL7K1VVWxqGTlQJdMXEJ7Zb3utc9prSDu6%2BSCqrLLQtvAfpFnXlxRU7SnsdcPm8ZHYNJjlDj2vQ%2BevVXRj0u9X9oG5SHg4Mjp965I1iRNEhsiAV0g0F9FOqSUgihqSKrTyTeBSscJwtCAE3pJnjYybl6lU1%2BZ6umQr0RU9m%2Bq1XLWSnMVKFr0n%2Fv2CygoVIPr9rKYrc4p4OzZ%2FrlpWFfGBrzIOXyyuTNdHZa0QNtfQFNx9NPZOYPp%2BpOeOu9FX%2BhwA7B5W0vt1zzz8ZLxhcjDv%2FY6UpXk9FONSQhLW%2B1hXbpYF463cJnXKG7GPGkq%2FV2lB2CmiNAGLduE4sZYYvw4XXCSQQTO5u6ziGQg4s%2F3pUSwHPHkdfD6hwz28yTxLgQAzYsk5ypGv32XhhPmP6bh74FWcrzIGYo1bX8mlrFv5YeENbLAsYO%2B9UCvIYInHhKVYtYx5T2%2B60xaRtmQZLeujk6xuOIrSGJpv9bt0EuVttEqc4Mw1bPQ1wY6pgH4g49CNxjhbSLn1vky%2Fm8o6JqDbliDE1zTTcdVrRWg1xyVXtRzs7BvZeW%2BLpyttRJfcr3vWRLMVypQiv5RgvEK1FXVPXn%2BibczGfMHaycVfpC5%2FD6i9opW49vP6kxw32qlHSAtWGG2O0%2BTs2Eg1qpNVuc%2FkMNS4ubrosj%2FOObcd63OMNvr7aZEbrNJ1T5o0wHlNUMEY28o3ZAB0%2FIDhnKwILIuZXrX&X-Amz-Signature=0307cbc1891406f023d149fb3e397eb94fbb4ba9c22d04212595ba7d9345a4b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







