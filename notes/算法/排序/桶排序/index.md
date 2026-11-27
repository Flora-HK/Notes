# 桶排序

一般情况下都需要根据数据状况来定制 

例：

一、记数排序：

使用一个词频数组进行统计，统计“1”出现的次数，“2”出现的次数等等，到最后n位置上的数为 i 就代表有 i 个 n ，按index顺序依次输出若干个index，致使数组有序。时间复杂度为O(N)，但是当待排数组元素量很大时，实现起来很费时。（借助数组index本身的有序性实现排序）

二、桶排序

桶：一种排序时用到的队列结构容器，元素先进先出

桶排序：

1. 准备若干个桶容器，按顺序记为 0号桶，1号桶，2号桶…，n号桶
1. 针对待排序元素的个位数字，分别将元素放入对应的桶内（个位为n就放入n号桶）：然后，再依次将0-n号桶内元素依次输出到原数组中（对某一桶内元素而言，输出遵循先进先出；对各个桶之间而言，输出顺序遵循桶的序号顺序）
1. 针对上面输出后的数组元素的十位数字，分别将其让入各桶内并依次输出
1. 针对数组元素的百位数字，再分别将其放入各桶内并依次输出
1. 完成以上四步后，即可得到排好序的数组

优于记数排序，n进制就对应n个桶即可，但是也要求待排元素必须要有进制。

三、桶排序代码实现方式：

1. 先通过分析待排元素中的最大值，来确定需要进行几次出入桶。
1. 然后通过循环依次对数组进行若干次出入桶
1. 出入桶实现方法：

a. 设定两个数组 `count[]` 和 `help[]` ，针对 `arr[]` 元素的某一位数字，将某位数字 i 出现的次数依次记录在 `count[i]` 上，然后对 `count[]` 数组进行一定的操作：将0~i 位置上的值累加，并将其存在 `count[i]` 位置上，这样我们可以得到 i 位置上的值就是当前待排序数组中 `<=i` 的元素数量；

b. 我们对待排序数组 `arr[]`从右往左（可以保证让元素先进先出）依次遍历元素，其个位数字为 i ，则将 `count[i] - 1 `，得到当前数 i 完成该次入出桶后的位置，将其放在 `help[count[i] - 1]` 上；

c. 更新词频 `count[i] = count[i] - 1` 。

d. 在依次对每一个元素都进行了如上操作，保证已经遍历了 `arr[]` 之后，将 `help[]` 倒回 `arr[]` 中，进行下一位的出入桶排序

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CU5WWDP%2F20261127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261127T103501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIGqUit1GldCg1fpKH%2BZFzFTy7wSG2H6dOyQxgf9LnfJpAiBz4zYwYAUjyrjYK4Dgr0VyzLZ4hou6e51hlVTXb16mASqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMY0mFTnuSAanCrUneKtwD2LJ%2F6a%2BT%2FAl%2FuQ8TEBgDzEIYWsVNPEBxVakFZtQlciaCOpv7ExTzkFcZr%2FIOWtPfrbrpvXl5Z%2FSojGvmdUBNUFTC6GT%2BXI5LCzqaqzOZhMTfySRpjjIOF9p9uOK%2FPs4ZHxrYK5kCMy05gcZjHbqPEhiNsPgFwjiS7TJEI1MnEkfVlyn%2FtnnqoAcwfnf%2BS%2FhR10WSCIz2maOLqtFYH%2Bdstt3CRx%2F9X1fplWaSf74WvSV4u1R2jBHxW9xWWu10odYLDrsx%2FwHA5uLmqFljNoYc0IoMOGwwUsYyR%2BvbG%2BAf5CvNAVtIETLkFNC8074Bzyi5hHfcesCJn1bgC6PQI4HTU%2FAU7JIN%2BzZRdqKlibWONS2ApSg3ZdHznCyS3qC2GGH2DSbKOqpvcd6iOyBtZbPFx6kyUgZkwFzF7Y0ssaNfxhsxJa7M5cMz0NGFO8oRl%2B4DIJuSZW3NfQTRup8kmZi8ADHcGDT8evso45uoGqBRZ7cNd1Q5LmeuLgbHuYbKGB2wT1NZmtJQubRjG%2BjRgeRw%2BjlNeCIjrlb3S46miIVHMimANMqpWqjbAZ6o4TdmIBAGxdCfXNyZ60eTl%2ByvP%2BobXIBiEywvkMGWyEJ%2FZSx72QkwTrHY2KKSepizU8ow34Ol2AY6pgH%2BgO1C4xkPc2NEHkudE%2BwZo%2BK%2BFiHZzeRZkvdeDL5Yp2Rp%2B4wJ%2BAph63k8aSAB6zvvayFk5eidaRQL%2F6slx7Mo84V7oJhuwK03a6p%2BOl9lJZ%2BnWW%2F1p6j6eI882FA5w%2BMptAnq3AVS13llL%2BSf5gfVfKitkaAgbjjoFgsIu6p3%2B4DG87zI%2Fcz7%2Bjo%2BNnKILF7ifBIQfaT6khUb9LXPc8uOFIHXDhb8&X-Amz-Signature=2bc3073133a4974950ccd89b6a75917e4eb30035d8d91c81c254a8e1d3c5bcec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CU5WWDP%2F20261127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261127T103501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIGqUit1GldCg1fpKH%2BZFzFTy7wSG2H6dOyQxgf9LnfJpAiBz4zYwYAUjyrjYK4Dgr0VyzLZ4hou6e51hlVTXb16mASqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMY0mFTnuSAanCrUneKtwD2LJ%2F6a%2BT%2FAl%2FuQ8TEBgDzEIYWsVNPEBxVakFZtQlciaCOpv7ExTzkFcZr%2FIOWtPfrbrpvXl5Z%2FSojGvmdUBNUFTC6GT%2BXI5LCzqaqzOZhMTfySRpjjIOF9p9uOK%2FPs4ZHxrYK5kCMy05gcZjHbqPEhiNsPgFwjiS7TJEI1MnEkfVlyn%2FtnnqoAcwfnf%2BS%2FhR10WSCIz2maOLqtFYH%2Bdstt3CRx%2F9X1fplWaSf74WvSV4u1R2jBHxW9xWWu10odYLDrsx%2FwHA5uLmqFljNoYc0IoMOGwwUsYyR%2BvbG%2BAf5CvNAVtIETLkFNC8074Bzyi5hHfcesCJn1bgC6PQI4HTU%2FAU7JIN%2BzZRdqKlibWONS2ApSg3ZdHznCyS3qC2GGH2DSbKOqpvcd6iOyBtZbPFx6kyUgZkwFzF7Y0ssaNfxhsxJa7M5cMz0NGFO8oRl%2B4DIJuSZW3NfQTRup8kmZi8ADHcGDT8evso45uoGqBRZ7cNd1Q5LmeuLgbHuYbKGB2wT1NZmtJQubRjG%2BjRgeRw%2BjlNeCIjrlb3S46miIVHMimANMqpWqjbAZ6o4TdmIBAGxdCfXNyZ60eTl%2ByvP%2BobXIBiEywvkMGWyEJ%2FZSx72QkwTrHY2KKSepizU8ow34Ol2AY6pgH%2BgO1C4xkPc2NEHkudE%2BwZo%2BK%2BFiHZzeRZkvdeDL5Yp2Rp%2B4wJ%2BAph63k8aSAB6zvvayFk5eidaRQL%2F6slx7Mo84V7oJhuwK03a6p%2BOl9lJZ%2BnWW%2F1p6j6eI882FA5w%2BMptAnq3AVS13llL%2BSf5gfVfKitkaAgbjjoFgsIu6p3%2B4DG87zI%2Fcz7%2Bjo%2BNnKILF7ifBIQfaT6khUb9LXPc8uOFIHXDhb8&X-Amz-Signature=14c11dcdc1b7b59389c0484ad24e9bcdd23e590b3b1e288a4ab2022f4dc7611f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



