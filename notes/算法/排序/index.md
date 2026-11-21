# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RE7IDMXQ%2F20261121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261121T091632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQDfOMq%2BoqPW1s7Y%2F3JO0VIFOm09rDTs%2BXdokJSSMmKszwIgMwbirBT2JgjLv9iU7aPiiok62XkaTrUZTxoVimyf0LMq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDK7aGurQDDUChBPoVircA6sk6VeF5ZbfsFK04iS8hnj8YiMMx3frTMJYDEdHY7f6dVkUOA9iHLP8qiME%2BTssl0Dc9y2IunbxE3fnZeEoGwdec5h%2B%2BugxqD30Pr2dLGGZSphyFyjpAhAgvGbLKk28HuFkBM2sXAVqetvHoXvupoO6oSGw71GfJ1%2BzNFK7u9E561JUeLMsQhuiYjplsg3hhOS4VdAuoWsHhrhmquJJZJ7SNArUUOBGooMhEboSP3nKXKuofkBfiOGBmRJT7Q0Me7FVXxj9mpzCS%2FnEMOqBTX4jMhJ7n3b8dho06b50Z5kFVaof1gW8um6tLoIZgGVJGAmgthhlVmauQYUp6LTJ9bz5JlVR4BYICJtQGs%2FFKjErBPD8lBNyAYuZn%2Bph7afmwX2v07sZHqWnU2nVcgsTAXlcIjdiMfG2cIQZYh%2Btr01SUBJ%2F48juTh74VsSZFF6vQ4izsKai4J1twcMjb0eS0RR%2BPJJQZo%2BoKk75LwcsFo55%2FjEZBWc0K5hFaJTDDnCq9VDTRu87CYrnrsbexB4sFkoTHAL8zmNGdb9FIuSamyZKtO6zVYXW9sz5nMsgBlSPGM6Km5UEgXLf1NPqLSacph%2B48rzLn047tMxHmwQNMSRy4m9IeHP4QDBrQ95OMJe%2BhdgGOqUBGBZda6Dt2DpNGr%2BgCAroMM1gzSx0bo3Mn2LIqvHuxXdBCnxBxPo2giomfVQp2V67JCvf9e3GxZ9kdpz2gnlpQx8AJCsvpBh9zUbLhbjSIr3jvdqMRTSxdnxGlC9KvXeTLWKIfC9qcnagRyMF0MAbEyMcXVuRVdrg8QooilrJheBzoe0dieQb%2FZJE0bu%2FHqFLUYO%2FRoUdCXPX1olvQPY%2BzVgvPzx3&X-Amz-Signature=9c989462ead429cb186ad2786aa7be5c9e2f725075081cd4546014a0b700bfeb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







