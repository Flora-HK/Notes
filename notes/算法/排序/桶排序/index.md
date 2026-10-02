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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667P7JKTPS%2F20261002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261002T075915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCg30ZXjnbCN0%2B6WcxPEsE%2FtGepvSdpMCMIbC%2BUemgehQIgFcbklXVhUDl0Kc%2FyCjAwTi703rnenH2qz0jS64OOl7oqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK%2B1ggmy3tObQ6dn6yrcA%2FHeHCMWq02SSy0NvsYAhK36fOfxiBw4mSG2jcH%2B2j38ulLMoj7QJ4gTYSsftj4ENpoY8%2BjpTnChEf%2FdxLyH4ZH%2F%2BdNflurmYRVlDSPoqBfbJaerkR%2BYiMBJeg%2FZtF9B0oriR6xMr4wKC%2Fl2Df5RW%2B4YgS23VbHQ1gq%2F%2FZIBkDaEcqiMp%2FS%2FiyASWW%2Bs5dP3pHboZQ9Ck4FvW5PF9f4XyG6WyGHwOmJ14lU46iBLA%2B%2FfnaFUTkIlkxxnKoVX4qVS9C5r5d6LBYAi3viAHYaFQTN9O2YGkbpTbAR8LnGIeHsGaLjqfehoVvnotIHDOHI9eofWNpKQ2yYS8NXcgHYsQz0Y7zcGfVgqNAE93PGiI42oKCkAEMFzTvgJYBM1c96fswX3BAAimQC3%2B1NLIzuyWgWybuL3Of8jSBtSnDSa07Dky%2F5%2B1DHvHmMPo4PJCLijUeNYV7ermAlfQ2V6cZxO8wmrq2zvzGGNPyretZdfuotOd5kuFKd%2FWou7y9pzM6b4%2F%2Flzw%2FnQPpSsz8V8QHo1AhVmDm5UxtOW5Syq8O3yD0AnBSzJJkzCUJTBzF%2F4b9b1lBRDmS3rJH8m8y9n8Kjt933rbuztKa2oxXVXSoKnXd5jXDJ%2BlTTHL1%2BswmN1MOqb%2FdUGOqUBTtaY0pYWxVkXjubuYitmbCJ6nQf17tyEWKG8wlcNwi9P%2BsJcKzOiDrYpCu%2FKe3N%2BZ5MyDASAMMy7nsopEK3lKfi45VPhFJzpDTcLABPwwbNuVAH%2F5IywuGzu1cqKPZ%2BLp%2BJXbCk%2BQQrjbQ81f5h9YQKT5SIdC4h0BH6eME43eT%2Bd4t5hjZ0UTaQhmdfyAtGUG0CFT0MBDE0yn01%2B5tyyBBnEUtXR&X-Amz-Signature=a8c129fb2feae7e865f321d34cc18d18f99f638edceb354f02addb5797607209&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667P7JKTPS%2F20261002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261002T075915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCg30ZXjnbCN0%2B6WcxPEsE%2FtGepvSdpMCMIbC%2BUemgehQIgFcbklXVhUDl0Kc%2FyCjAwTi703rnenH2qz0jS64OOl7oqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK%2B1ggmy3tObQ6dn6yrcA%2FHeHCMWq02SSy0NvsYAhK36fOfxiBw4mSG2jcH%2B2j38ulLMoj7QJ4gTYSsftj4ENpoY8%2BjpTnChEf%2FdxLyH4ZH%2F%2BdNflurmYRVlDSPoqBfbJaerkR%2BYiMBJeg%2FZtF9B0oriR6xMr4wKC%2Fl2Df5RW%2B4YgS23VbHQ1gq%2F%2FZIBkDaEcqiMp%2FS%2FiyASWW%2Bs5dP3pHboZQ9Ck4FvW5PF9f4XyG6WyGHwOmJ14lU46iBLA%2B%2FfnaFUTkIlkxxnKoVX4qVS9C5r5d6LBYAi3viAHYaFQTN9O2YGkbpTbAR8LnGIeHsGaLjqfehoVvnotIHDOHI9eofWNpKQ2yYS8NXcgHYsQz0Y7zcGfVgqNAE93PGiI42oKCkAEMFzTvgJYBM1c96fswX3BAAimQC3%2B1NLIzuyWgWybuL3Of8jSBtSnDSa07Dky%2F5%2B1DHvHmMPo4PJCLijUeNYV7ermAlfQ2V6cZxO8wmrq2zvzGGNPyretZdfuotOd5kuFKd%2FWou7y9pzM6b4%2F%2Flzw%2FnQPpSsz8V8QHo1AhVmDm5UxtOW5Syq8O3yD0AnBSzJJkzCUJTBzF%2F4b9b1lBRDmS3rJH8m8y9n8Kjt933rbuztKa2oxXVXSoKnXd5jXDJ%2BlTTHL1%2BswmN1MOqb%2FdUGOqUBTtaY0pYWxVkXjubuYitmbCJ6nQf17tyEWKG8wlcNwi9P%2BsJcKzOiDrYpCu%2FKe3N%2BZ5MyDASAMMy7nsopEK3lKfi45VPhFJzpDTcLABPwwbNuVAH%2F5IywuGzu1cqKPZ%2BLp%2BJXbCk%2BQQrjbQ81f5h9YQKT5SIdC4h0BH6eME43eT%2Bd4t5hjZ0UTaQhmdfyAtGUG0CFT0MBDE0yn01%2B5tyyBBnEUtXR&X-Amz-Signature=cc7c8ecac03456b43578bd69337eec9a5d8e96fe3c69214f2869c1371ab3dbff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



