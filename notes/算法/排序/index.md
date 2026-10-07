# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EQ73Y4Z%2F20261007%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261007T081253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIEvkj7qiJCpurl2d5zp%2FwZsUO7M8xYLVsrIYViSCZJuZAiBe4mXJhr2z%2FxfQtxTdyJg6Bh3ZN5GZVbIkjjpxPxCnzir%2FAwgHEAAaDDYzNzQyMzE4MzgwNSIMGjhTTzJkDLXKSXVvKtwDap91jR2T0mOA%2Fn3IKHsW17CFE5pANWjWZThk2Th7A%2FjxWxFSxS76on4AW5JDB8VT%2BJa3%2Bkdkii%2Bdy0lmWvOIcpWIKcxUS75LbSsJeNWb3lCIYnQ76G5LBZaR3rC0NqQuOn3AOmox7gPileEdXJWFfuz%2F50dvft8Q0faWGl0ZJ9JrmqINVNtOjXuEQFjmAS8Q8UzUD87PaeR95wzKSHk2Nervv4iDJjQ3RHEzQmS4yAKhwXDjSHF0emWpnv7MFyzCRoAVBouN62GlUdNSUlNpIcg0s4n3w1J37m07DIzyzNJlEHAewkKTJ7JU0DLP8dhote8oCnxEG2wwKYTSSU1cDLqsYj%2BW5MNVCBCzRtltU1q2L%2FcYF7AVug24ojJoMb7v%2Bk0iCysEP%2BDAJVMIy0XF0EAs%2Bcy3tWdTyw05oDS4fn4WjnQzVEC15Qmq6HGBt87cCotah9kaUu2IpjXlA1TDCDVwK2CkOG5X%2BbqTXPre4BX8Ns4Gz1yyCy2zYGa1gO7AL01g%2FrJwwdbrCRTqfmgvY9nth4UD2TGxnGU75xbGWUqFRTqk8HSzdggeW89cGlXfb2jQvIGimxYn37PRE9bSoGBuISaUAH4GV9kDbAWRcSSjDQh6j681bdEU4cownsuX1gY6pgGQ5R3TOe6Opt0Pfh5I5uL3zfKofYYjRbZ6vqx14P96PC7dRMGM2%2F9%2FTmWoj%2F8KpuPPGJcwAqQI%2Bb80pNO0s9eP5eSzDUIXAGBehaJfFYcOJLpq3rnj0pp2IteexbvzYbkcYzKKJ5Ry4qLEMJrupoOpyyEnpndfxEkVE%2Fj9PelKuKG3M6zmWb1JHLpHDy5ee0oxsKHUEBj%2FDCj9CrSBWVBcDHf8Ts%2Fc&X-Amz-Signature=4c97aea815372499d3aa1b9072f08f3330822656236ef272c885458265cf9755&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







