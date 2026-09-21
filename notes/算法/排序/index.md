# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFIOECQR%2F20260921%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260921T074109Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAXTmXb%2FHcWzC%2Fpt937c4GfMwmEaNZ%2Bp6gyt4yvEFLvAIhAK7d14LQhls0xqZ9eilkOHRKgMFka85oKmpsyBT0xw9pKogECIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwSUc9z%2FfitFOnW4pwq3AOjCpWv00GuBFmyYKEeALvEvRMyiU%2Bny1tLX64BrgSLYPmqb4Rgt1P%2FZZ3Gdxe0990rl9IZ1KWLbs9jTvcJPur1hNwqguL%2BVxlH5opEcTmie7n%2FM5bKqxRxyOC2avCSPd9Wv5WhCVPTgKeAOpaRTC1INc61%2BQX13y1zyXlBB%2BLJDOZfDPsBph76FJugscZ3fRi11We61Y%2FICk5iYvLR7JAfbSvpnFBEXlCB8GXcwqSHm28%2Bx22%2FVE9Vb31UWTgQ9YT4LcT6rTpembZKENVRk2EREcGdWucfR4SJdcnxtrEaPHQqxVGY5oqINyDBzXQk5fHBuNWJ%2BbPCe07ya8MkQx7NMX3RXb%2BzU5L8%2BlaZ5dkOapF81iPB6tzZcJvtMDegcP20F1I%2FO2536tdv%2FVOaAJM43TwxssjMaSQooBLMGyP8EBCT%2BOpdpMWLOrmwUQYoAaomTBNFEtjdCgRc3mGp7122wATJImW73fOoEDXjB8n8Txvoc%2F%2Fu4ytOn8V2DE%2F1NdkP%2FD7zW0bTUSKEoVlvufZ8Gwen5HunRHUOnaiFGAtCLzlTxTdcca238HdcRSQibN4FwsdPRRUsIXBwTsLlMmYPWF45NWLlKRNtipx6YUb4fj2h8VHGrni8wvCeazCgrsPVBjqkAcEgDT6rlSKXRLec11WPS9qelK9NBUpDpq%2B3ocE%2BNaYOYhkH09u%2FvsNb1TS3DKZ6k5jPA3VP%2BGBU0gqZa6%2FmajPV6koDfvLXZTP9MsEWE3fdQ48L561DJ5Ecxt0KL4gYU%2BzFL50K%2FBHlCDh42VHfEWAl4aWMLteKvOzptqrAL%2FUDZsOf5b2dwQ3qogAnD6IFhSOcvUAVJw04buz%2B6biBimi4wYWO&X-Amz-Signature=1218dc90fdff7716ba0f3201d38e34114e75fab0c8dff63502368616f6632c81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







