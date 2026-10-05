# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZMF2XVV%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T082729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLXdlc3QtMiJGMEQCICk2RAo0eyTuK%2Fjrs8S2%2FUESzSnpAJNZartjOUli3XNoAiB%2BxbknHjUmt%2FVO2%2B%2FsnYJaIcJYOEnJqiLW1ffj%2Fj2UbCqIBAjY%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgOpQpSpaKG%2FhDGqHKtwDOSOLfXKGNE%2BcqDo5JLmv8OIc6otyA6gN28vyqjEtYNCPvRpWd7tU81iahoGyAMeDhFSZX4uwmMjOvQPBX2GoxCXwl5XFON4OGK%2Fc7FGp4nab%2FTCezGPg%2BGUvf%2FA8fffKs7js7GQQuYBXg9Ue%2BR2HtozutMpXBl0EcLNfCzz%2FPzYwWXSoJNuFPMuAnujpUf6jDMjTKkZp5YQwSHqt0063XfUZ3oWe%2BzE7T7XYQbpwOpoA8VBhzaF1PpsoIr4kZ3HYdxRcHj%2B5LM%2BQIqFN2Xs%2BSOYrqddSZghxQDyJRDnuAdN3Wi2CpoL6l2T7BgA83hHpsWruECrN0%2FOwCha3InWkepwjk0tL5YrlQRg8Kzkzm%2FG2NlvHxwWXkSI1rbyZ%2FDYgX5LuD%2FhmG29AFVTVVLIKK2INA2M0gJ86kuIS0p89Li5SCrYc0EA2S6iThFydJh2wCeH%2FfX5dzZXALdKH1vCYhLLl%2B00DIKRzRP7IclFaGu%2Fl7ixgR3FWLjG4W%2BMMjclLWY91DChunZ5SRSaWC3yDztAIL7lq6al7IhPTLnI3Ydpk2ODqroglp40SiR3%2FJlIeUVwZA%2FEaRna2dz20ZCMGekR4za7LpA4zkUFNNs5bFY9VI%2Bmwh5hhTUZyUDswqpuN1gY6pgHuWs6WeMmWIeyl8wiCe5SQ%2F8yCJmyCkpYtdwQ70xBF84v0cjA1odpiZvdFJRvbhIE8y0b73v6mnzrOXvlEXM4uYantn8NUjZwyptXMauSxrZ3N1aaWIecIRnjBUyJ%2FPhKweli5MSDyDPQB3AeoeJjPuvPPGU0VuFOLjLfNFIkr6U1zB3PeUDWhkgDzdB2UFSnGHgd39kakJMyQihXGScWC63Q8v4DY&X-Amz-Signature=c6e1195c5becad0c8d99c6766588b43ec4bc56aa4532de9696171aeead17ed3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







