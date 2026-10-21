# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGLYRT2V%2F20261021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261021T070806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHjAJkO4O9iw9HYVLZPH8jglCMKU3cx%2BaV24j%2BvnXE%2B0AiAGDnTaIJdh%2B4USPyvQEgA0%2FSBv5ujV4WHwf6vSlKa4cir%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIMOk9zuLu2pWtowt4kKtwDM%2Fk4s2lnsLRA3tAaYTp0Ept8NAst47GXjQpaF1NT5bVIZr8nEiks84URWIh3Eq6dLHLtsc7lvsGmKclW2elD%2BwEzyL4L1OipkYxvGKbPHXxh8Jc8JPBBGMVy%2Busit3Zf2E13AMxNeMxE9Qu853JxBTjiAeoCkEyCNEBXnZ40nsmQ6EVnvSCtQIGrTJU%2BNblJOJKkgALtl5Q9308jvR2Ka%2BuNgIhA3sTLaS4iahbGWSdxCrNwJHhQpFDBNxgyLqOzxbHq8C%2FMEAD6ueVMS6vYBVP7D2AZqAL%2BtnyVaQisf8LNXsq2mAtOU60LYWW4kC8PrvrgT85br8qNllWpIeXLGmEphsqW61CNw%2BKn5XPL7ax50sQJoPy3QXXAp3OiiCt70dhwRg5ctaoOd8qYSy%2BqqEt6OYJkOdpik3yMBKvOCYhyMMD9NEp3Da4tToIj22s3KIquDh8FEuYPWEmHy%2FBskGOheo%2FtaWIC5SrLdo02ghCvmNOyxgknGstkf4x2PdAPR3cwpuNmM28hK8aBQfE8c7FLEqeimwkfggbus%2FPA%2F8%2BJq00QeYPjtPDdx0OugXfvw0%2BnmObnd6ViC%2FD3Ix17dhuti5feT%2FSterUu3SgDUqJXJYYE5VpdWGm6Pyww0pvh1gY6pgFEWizNdgamkzPvxYdyJz%2F2HfqeLDeG4Bg%2Fs6XjKEYApJh%2FPat33FDMawsy4jH7KS4BreB6h8re%2BXAjVfbghShumDmKi4TUfxvUR%2Bh5NAyhWWM1m5xyOmQutV7xh28PZBtQPo0xOLqHdpgDRoBMbWELXsJTHbRNr7pwRQ2EtxAHwug%2FMzMsuGKeIp4%2BkLyigpQbPmNOA8HKr66rUHrkQ1pcfoDIkbag&X-Amz-Signature=d35b0f0bcc757d9b279805bf00bc48fd8da6f5105e242025ab15b896103d5805&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







