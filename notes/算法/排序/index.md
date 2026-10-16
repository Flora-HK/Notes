# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VG2JX7TQ%2F20261016%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261016T064651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIDJdhPH%2B78D7wlcwUBxx1J6621A2PDi3dM2%2FcQ9kPM2tAiBTxsYUqPzwOgMgZW7qAko05Z3TJRM4kUNgqbZSHH1icCqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0ekH6gNMuQ1KY3hFKtwDZsrG%2F7fO8hnHa9JUhCl0EG6mJVb%2FDeFUzPQMQGsZodBmD%2FMzQezOC1QFDJmEbyqjWhSPceS0gHBAUyKsaGH9b6d5zEDBn4aBvkXQcWfGY131Pxq%2BTy3Ukvh5ijyeFF5clvcqu0K3ZG0YXh81A%2Bj4a%2BJXekt3jEerh8NvRLOJZiRbWhajXL4jOdyrB%2FdJ7dmHPNKedwUJNngMQX3aoepZeshbapOwwRbYKJhHXKcVkNOJPuAlq6D9gLcQ68r9JbAAB9evMuC7cMloE2JbLb0DHE2%2BbeF9z%2FdqaUDSya8lX0v3e2pUmAMFvnu1pWDcWZIh8CaFgfYJO%2Benar6nl8JDFFLLTAFuAMv5fMYZRlZxOHFXKkRANE3OZMEbmQ4Roc5gPnaAAyEacMIlzotVCCDoXBKlbPxIdEpGFKg%2BFSz7QISb0XnTecPqdhFw12RSCpkbAI34qk0HjO0hHdyUxIBa7Zqs6hXnbqi30jcRibk09JUrNEHkx3nlL5J3JBCG8ds6wU3rWT9xYjfBIUfiuKh64NzQFzWx630pZJCHditdDt1MZcIFmIzsXIigPPrLoTBPbrlf8GhE4pDBKHsflbp4dyLEVeIb0%2Fq65HQebeVp9hilcmMKV8UAB%2BT8tEcw7tnG1gY6pgGTaXnSy07%2FJYMm7y1o6b%2B%2FQGi%2FU%2Bd6ajT54ndlgIahAdaeHsJVlBQPO0dTm0t6aNI5x5dYAFycHWWIXIu%2BtUrSPReHPVfJ7%2B2Epti%2BNBErD5%2BI1KAYV9KKUbMNMNJifNTFXq5BK6411xSIr6Av0HN8tcCoU7rdys6tqYaewI2wC9dwWsEAMidPsWQOdkfhZx12xGBxofPVFDVbUVeOquKFGnrtqhMb&X-Amz-Signature=4067a4bfc285f4a6c3469e3ce1579e954c2773776f2638f876191086e1c87baf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







