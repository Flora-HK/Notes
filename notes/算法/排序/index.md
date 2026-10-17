# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622DXUUYO%2F20261017%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261017T063744Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJHMEUCIE8ky8pm29cCrzsLZQu1lq8ZvEigmusfV62eNrHEinsFAiEAqic6jRacmNIY8TzBKqLJ0WMDNq0WKb0467dsd1ktVBkqiAQI9v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAxHpyyO%2B30PWX6bFyrcA5Xposfy1ESAbnLB25FN1PRrOUZR8VnKgHorlm3cAK1jXZmbs7J219vxyc%2BjasLkxEm6wI%2BUcU%2BRQO03ogNyvLNSqHM0fut4U4Xcs%2FimPRW3kzs7MXTpT0NQ2lUC9vn4EU2e1ItW%2FTDYckZtR1kTkRz%2Be6XwQ7WSQwX0uprnrlMADORlsjn3jW6pE9x%2Bauv0xWQ459GiN8P9h7nkdgMof49YHjlzOa%2Bwn7V3YeGv5vLgDxl6XMwxmucHVdKCqrwv2rMJvvspmgYuwureojCkdcWMA44weapsqXUggoq2SdSGTNWKo9i2AIfMOezxmX5xbM5iIOK299pxi2N68Va7O0mixWGRzwAy6Q0c%2FfVeS4Z4WsAKw8%2FnYn4E8yAKu0SA2S80%2BMci1kvl1Dh5gqUmJMRI0XoB7Xsk2NsiZcyy2Cq75HJSccn6Wj1cSw3Uwl21QsgnVLL3HfWbIpaJXgjJhh0a6ucIh2er39dSfzCwUhmevrgygVONjbowVh%2BySFZIspKlTwwJrOO41EeEP3t183VWt4mBRekjwRNrJ0Lm3CzkJ2AbEp2lZnVIPbe1H7p5UEiQZ1PJIu8uHCCnpFBa8Yl2JFb2uRMu25rd3H0YoBuuwsZisr7TYyZBr%2BC5MPiHzNYGOqUB0EQwPvGS6%2B12f%2FypN7umknGH4KfQ%2FAKe9772qU8%2BFVFd2gIpuVR0nQ6V0%2BN04TwEkTGaO9VsrEPU4f4HnxIegwUcBbe4YXn6o4QgBtKc5C%2BRfXCBnRGfTF7Dg8XQ6FxlFNr%2BPwkq4oCwVBgKYSFaZRb1dp6GXZZdO8TtO4Pfs5aOSDe5psMCh8EvaEVWMDYSZQveOYuBcrg3WFTauCkjba0E6qxq&X-Amz-Signature=322cc7147de9ab5d56dbe9288338d76a4a6b0bbc16d3193f10c40cc2a7081dfe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







