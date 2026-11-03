# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PVE2BT7%2F20261103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261103T090415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClM6Nx78wY%2BfhK4%2BUjo7VwAggEthWGDGw5hANtOUwEEwIgTSGT9J1jRSgee2JBTnZzo1AB%2Fj0lfY%2FuIgnOLoQWAagqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDQ3ALHEUyG6b%2BksDyrcA7y3pkIv3%2F5YuNbAJNuUXUSDr4ekvzT357fDUFf39mhyma4KPZha6oV3TZWOCHHw0H96wQv1bHXcf86e%2FowoQVDQvN9y2PYaXAO8TgyxRaF560HhlxRZr4rtNgCE%2B3tL9P2J0PV6qkYxFjqvgLIjCEd2iAq8mi%2BOfuL5hQQa6H9G%2FqRCt%2BHGH8kyeZxOCv10HuhkqEKkY5S7SILAXDGqfty6vJhPz%2BOHB%2BDWljoBetC39J5F0bH6yZfd5HZz8Hn3noBlV2NmGYu8B3uGaM%2BFMB4gB917iXzAoxSAaO0JWNO3aiJDzJi%2FWfyDWyRvgtz2xqN%2BhnGxJlL%2B4BJFbFctcMQAWGEdaSDx3rkKchq8B5cB0m8tbi9%2B7AJYinwx%2F7eukY6N85Fjlv0BHM9i59w%2BfEQZbkieTI7eTs4gBlHNyqX1F1O1XeZybszNew0xNbZXJuSrfOP9cKKzzykgrwviplb%2F%2F1PXLGOrLqag7JdZCh6hEZur21PejbiZpVYrRsjS0y%2FUyzeYBpx7gruW8holUQwTsBLuWB3MhyovGLiPeeYSi2o5cuJpDl1IwPu75xcImpcXu%2F5cCb5GzCj1n9madGDydKCuSLZmIPN9GRY%2BTFx3zOBQADLP6MTKUYWJMMKgptcGOqUB9i0hlZgfA5FCwQHkHUfqMtvpiqUbjnTusveoO8pmv5vxHfC6z2gEiO3MMc3hGIdUb77mm5xhX6n8rXvcsuUgjBeI4BHB9XXhZhZMIp47h33Pnlip7skpFgSdZngZSaAP10p18PyPcJo1WvHpDm8P3%2F7ahf0UB%2Fa4co11PtBA9vrM7Hex9Jkr5ixj%2BdiDbxIemBsP8uwT3mSGXoEQknG%2BOd1GDg3k&X-Amz-Signature=b73e16814b5a6e99337966e5d288ff16e4c2e688e82e2b5fbc60b1de58a85e3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







