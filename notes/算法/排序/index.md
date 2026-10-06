# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HWPAADA%2F20261006%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261006T083746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQDh4WOkNS0Gat2jjXWJ9ffaO0tCP2rfX%2BDU16huN9ByzgIgAZlvaJqh9ELcy7aOxP3fIoWeSq9m8UO%2FDdM4p3pGaxcqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBseZkP0ent9StfmTCrcA4wkv70AnNEFTt43QlXDbU8pDs3cBzKXSouxhQhtKA0fE56PGGE8l2MF%2F8mAlWlzjUU6wrMWUjt2QRTDK1Yl9o%2FdF%2F3j62%2Bg4gCvU83wQHodTRhv78hPPE2DTLTmSoCGSwj5sEfv36%2F677qsbcMPPRMs64aGaMuWoMhHwCLCBHNOSexZ%2BDV%2Buggrp%2BOqtoms%2BeTUP8LE7gJxDK0KsODAX5jxaIoSxYQi4pf5t9SM%2B9v5LdNHCNaFAb5DqJ40hlqd0lBMcr%2BaCugt07PrgzOafHqDRIiwqBv1vyeWH2hf3VDAvZzwzMPhi3yl4yz%2FTJ8rQkTOHXgIFlVFhGsp9pekfI4HNxwzECGPaHzDea1N%2BKMJFHBSWhgvbkM2LAKuRmZysvX9xEf0NScD95DD7GzpYg7AR3aZlzHs17OlI%2BnSweTTdPspF2nhkwi7K%2Fo9qNoJ%2BG2gCy7Mv8y6uZHKoVTHl%2FkqiG8TySZHZOvMEjrKY4Xg3WuBr1C1wi2Y6LVctL5eDlV646GkWVoGoXwFI9Zkg5JxdIeCIhwgLjE%2FrLZ54m6yU%2BzNinsOkaEUuaI9zXSre8Q7IOsT2Z6d1GKTKFiEHKmkFRuK%2FMUeT8KWPMb6N6PRrnn0mQGj6YDaF82TMJW5ktYGOqUBVTDLFzYxEDCqm9QPVOGmmRPNRoT3H9eHhcsSYOpUSRSv38pRt1pvpnRjfzqnXhPwbai08zI8L9emRhtNXbDIgP4uOBGF3iSnVzDKgF96Rf4wqkyRVvvyGOKAgfw1mr6K%2Bux%2B7nJwM%2BXnnMacCJHPBeVQpXZcTYWiNfF0%2BeHY59OGMSGdgVWL6hOcoqyPYAX3BI9SkboevwQ80Ll749JqpPt%2Bnycz&X-Amz-Signature=3f05babd6254b535379c723f93e76177a955333f71494a16665b8f9476ea4703&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







