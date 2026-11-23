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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LJQASPO%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T102206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGuXR7YZrlWtkbtTBoOQsl8J8%2FpI8Vf%2Fd2DmlrWJLD4NAiEAtS6ga2NNhg6L%2BAbU09PncyVAMsaG9bkb6x3JdlYDnrAq%2FwMIchAAGgw2Mzc0MjMxODM4MDUiDAh4WDtEzzvWsO%2F0xyrcA4tGvOHEtzAz2nZS%2B%2FZB7SgOBX2LL4N94jL9yGkGjZyuD5V%2F7%2FlcujZQnobbNFrOmUGxt4%2BmhImiLB43pLbnkm2P16GzQs2WXpI03nx9lTjKOLK7wXv68uaU2YisADPXjZ3M2%2Fwh63oIoV%2Fb5eTF5Xv0MQ%2FuI2ArjEr8JpSeQrK%2FuROyTkM1mwWhlW%2F2QJcfA%2B2XvqeaJvlME2IQNhkOwG%2BRFcURCPfoHUs1%2B4MTCR713ed915FHSVZtd8COOnW4clVGP7yp%2BkCA2HDlN155%2BRaHQ7%2FZaxABcvX%2F0MQt7IxiZTj9xj2MAfmnQ6ZAGfUay81rPl07c38Yl0HvLPmMA5Ig8opTrHMHec9U6vqsI545WXIwuTIqcR1CY9g4Wu6EqyhNZFpFjZ23MA9BBjFIvhR%2FFwqQpRbTkLOB42eM40IVHW%2Fi7WEbPBVY1gGp7Afktz2xF8u5cbOsfWaJcKp3%2Fek%2FpUri4yjGvUiWNY%2ByuK7ingR0zZWo%2FYhPJ5%2BSFn0vJLPohsmXC1co1VAQXX7%2FaGMwPryR%2FyBReDziSzfTu9i9EedqoSl6QRG8vFcHZ7PApWgh9qQq4F8EUbTO2tlriH1muNZnRNBRCgQXzMAaniKjTT2mvui3Xg%2BCmW1KMNyFkNgGOqUBNOWtmjvjowEqw%2BH9JXIS69QuEMxpV%2FG3vMK%2B7T8Dp94%2FanQOt9LG9bLjy8Kdp21bA1aLqnwxB4MV4UNqIPk5sM93i88fDjoA5rOfPBYq%2FaRX3pWg82IxWNqCWHGmwl0A6%2Fm071eze96UjGA2jmwx7wRxJD%2FqT80DeRu%2BWKoHmpKt2LgdMekvNssCY52EkHgnGSqaOtozM32Cdr0r25T%2BoKR2unVD&X-Amz-Signature=9dc12259694c6dc83323d4cbdb905a97923ed4eb762f033dba4a7b8fdf92ae8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LJQASPO%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T102206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGuXR7YZrlWtkbtTBoOQsl8J8%2FpI8Vf%2Fd2DmlrWJLD4NAiEAtS6ga2NNhg6L%2BAbU09PncyVAMsaG9bkb6x3JdlYDnrAq%2FwMIchAAGgw2Mzc0MjMxODM4MDUiDAh4WDtEzzvWsO%2F0xyrcA4tGvOHEtzAz2nZS%2B%2FZB7SgOBX2LL4N94jL9yGkGjZyuD5V%2F7%2FlcujZQnobbNFrOmUGxt4%2BmhImiLB43pLbnkm2P16GzQs2WXpI03nx9lTjKOLK7wXv68uaU2YisADPXjZ3M2%2Fwh63oIoV%2Fb5eTF5Xv0MQ%2FuI2ArjEr8JpSeQrK%2FuROyTkM1mwWhlW%2F2QJcfA%2B2XvqeaJvlME2IQNhkOwG%2BRFcURCPfoHUs1%2B4MTCR713ed915FHSVZtd8COOnW4clVGP7yp%2BkCA2HDlN155%2BRaHQ7%2FZaxABcvX%2F0MQt7IxiZTj9xj2MAfmnQ6ZAGfUay81rPl07c38Yl0HvLPmMA5Ig8opTrHMHec9U6vqsI545WXIwuTIqcR1CY9g4Wu6EqyhNZFpFjZ23MA9BBjFIvhR%2FFwqQpRbTkLOB42eM40IVHW%2Fi7WEbPBVY1gGp7Afktz2xF8u5cbOsfWaJcKp3%2Fek%2FpUri4yjGvUiWNY%2ByuK7ingR0zZWo%2FYhPJ5%2BSFn0vJLPohsmXC1co1VAQXX7%2FaGMwPryR%2FyBReDziSzfTu9i9EedqoSl6QRG8vFcHZ7PApWgh9qQq4F8EUbTO2tlriH1muNZnRNBRCgQXzMAaniKjTT2mvui3Xg%2BCmW1KMNyFkNgGOqUBNOWtmjvjowEqw%2BH9JXIS69QuEMxpV%2FG3vMK%2B7T8Dp94%2FanQOt9LG9bLjy8Kdp21bA1aLqnwxB4MV4UNqIPk5sM93i88fDjoA5rOfPBYq%2FaRX3pWg82IxWNqCWHGmwl0A6%2Fm071eze96UjGA2jmwx7wRxJD%2FqT80DeRu%2BWKoHmpKt2LgdMekvNssCY52EkHgnGSqaOtozM32Cdr0r25T%2BoKR2unVD&X-Amz-Signature=6269fb48fa32ca46512393fc83f598be60b5aa6d7a99eb207d140df9a221d8e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



