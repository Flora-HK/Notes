# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VPA36AZ%2F20261108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261108T083924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJIMEYCIQCEXO8OGZHJkDZ8z0k13fhLjIsBwX4cKP1uDNqyHKtFBAIhAKf7ps4kKeeDh2StO2s8FFNFT0yH2t5IZwWYvIp6YH5bKv8DCAcQABoMNjM3NDIzMTgzODA1Igx%2FaHTvwinQ%2FIp5yW0q3AOKTCZQPNNAPXhal%2F0zmp7YLDGeNC6oQdpN5DlTWYCaSon04ed8aYaf8WE01dyrq0auVOP8jTR9menYPCGV%2FqlpI%2FcY3TzIzdbXYT5fOh7W9zDcoYK1LFnDXNz3T6nO7RGPc4NVyV2F9nwcyYZlpaqKS%2BIybg%2B6YG9IzMdy%2B%2Bgw2hU3dnlDyvmxdvxH2rTWEAzthLvfV7P7D8vjbY9DWzvw6xAFKxtwr9okjcVm9ZcFy0Fukva7W4gpvXuWU99cXVpVYG36k1Nj3tqJmq8EqlSaQ674zM6Jzb9kPnJDk57Sxjysyu4yUSnlQifHdevS%2B5%2FPOUP4jvZajOhqgdjWzB6KCBVm9zedSIq89e%2FDkpvzj1MgyCI8PeuFPsU27qq6QltkJxj0C2%2FzimF9hozLqSVZiYnFynskXt51h8pwaO8wVl2RM7l6ab9P5p5R5j6d6j1fzgTY2kfTDNJZRoTciw5uSpmFi5OGfaF%2BJgH8tJRvBnxJon9bYz%2Fn2KiVbCbTY777svlkqGWlzbtHAftBwoKH5RBrDBLJ%2FKFGoz8K2aC8OY4Fd856Nerey44a2LAa0N32MfTffeNEEOYvGZKFDX9ANeg4aoUKVildPq41shS0liYfiIrqKBxocXpUMzDst8DXBjqkAfn4TZTLUP4sGIIZ8A4vABe7izd1jAuzAGIe2VqMP6bnm%2FKC7LzyI49hnPAXQiSkomFjCl9C5mqztIMIILsvYNW6gN8Duw2jfDYgbCPEwcRV%2FQL5sse1NUM7SJCYFRaqD3tvsY%2FVaZ8yeUjL1jddr20HRNJM4L7PFXCdUX%2BpaTCrG4jOxjsW3EpBppEEheM6nbbLJWlgDsFseYpxFOHhAyZS%2FwAI&X-Amz-Signature=03f7617463d4dffff98b3354c9f74175970180c87e05010a720be03cac1b6744&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







