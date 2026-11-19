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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PFLXMMY%2F20261119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261119T095619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQCenxypEO1Bo%2FLvx9Bi%2Bb%2FRlx%2Fm5mGVjzgQqblkqtC9JwIgSx9TSdleuFTBNM3WWxaIaHMJRc155LEcK8EbBlwmJtEq%2FwMIEhAAGgw2Mzc0MjMxODM4MDUiDIB32sEaneYuHlG25SrcA4b1cvDh84NrP264c716b1pg6DBlYnHP5qbvep3%2BSQDi31Ia%2FFnj5F3Z3eXD1CgjxfeG3J0ZakpQCpd03KCJx42UtUTL6ewZAsvNWtOq3WPmvuQVAyYoyuv6g4VP0Q%2B1dl7ZHrGegk5LH%2Fc3i3t6LcXLESTNv5ZivVIMCNwccQV2rynB9ziMM%2BInUarRushyoqg19DGFBoHn5Fdy2KEmjRyoZKHQVTZGQ8HSZy5NCdaktzWryCLhXhtTgoUHtVMMVjVqTIiHV7rwGmdSAohY7ivHmN6Xu2r6N3MR7HLrOPT1bm1Rb3Waz5eDcT6X33awDCQrUOSRmHgi7bmiB4b%2BpraiAjm9S29JUFIlzHUUTxAIN%2FgPsgHat5eOpBjUoPp83KShZn3etEOJ%2F19YBhZNUvajGT1v90tZyhHEGb9fWD%2FKU36BqY2GIOBQcGLhDgc4MrW%2FEArlnz845Zh7LPuFeAVIV3ChbaaTTGmcSzYFFp1j0nJJT9N%2FaPRIZ%2Fk%2FG9wCMVpeUdV8F6X0Sk9FAKSjI7L%2FAp07FzAc09asUQSyddNN0IQFgsMHla0%2FLV2MCrGPjvcfBn%2BmQaJ3FEte1UzgT0tu5fc7%2Fry4ZB2hbjXNlNdumPJ%2FtKs7EjTSdk%2FsML%2BC%2B9cGOqUBYP4XpRXMswzqgQHahsjzueJqLGx7An1O%2FwtvxwlMBBDwVoNyich8UFSxTfo3X48AnfaalQjQP34vxDtGHk0q3qAhr61%2FUyvSCnC5A4NQeXNVnZTcVtVu3%2Fob3tW7%2FgwdkXe%2FBer422f%2FenIjLI1yrjqUJd87rqC3sX7zXI4rPgRt%2FK%2BzqZdSesdIbFyYurTwItqCAXr%2BeFcMgY6OIwB7hqLTtkd1&X-Amz-Signature=b1268af315bf79e738d4bc9806746c1235e592e846b8a899bda559ac898342ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PFLXMMY%2F20261119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261119T095619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQCenxypEO1Bo%2FLvx9Bi%2Bb%2FRlx%2Fm5mGVjzgQqblkqtC9JwIgSx9TSdleuFTBNM3WWxaIaHMJRc155LEcK8EbBlwmJtEq%2FwMIEhAAGgw2Mzc0MjMxODM4MDUiDIB32sEaneYuHlG25SrcA4b1cvDh84NrP264c716b1pg6DBlYnHP5qbvep3%2BSQDi31Ia%2FFnj5F3Z3eXD1CgjxfeG3J0ZakpQCpd03KCJx42UtUTL6ewZAsvNWtOq3WPmvuQVAyYoyuv6g4VP0Q%2B1dl7ZHrGegk5LH%2Fc3i3t6LcXLESTNv5ZivVIMCNwccQV2rynB9ziMM%2BInUarRushyoqg19DGFBoHn5Fdy2KEmjRyoZKHQVTZGQ8HSZy5NCdaktzWryCLhXhtTgoUHtVMMVjVqTIiHV7rwGmdSAohY7ivHmN6Xu2r6N3MR7HLrOPT1bm1Rb3Waz5eDcT6X33awDCQrUOSRmHgi7bmiB4b%2BpraiAjm9S29JUFIlzHUUTxAIN%2FgPsgHat5eOpBjUoPp83KShZn3etEOJ%2F19YBhZNUvajGT1v90tZyhHEGb9fWD%2FKU36BqY2GIOBQcGLhDgc4MrW%2FEArlnz845Zh7LPuFeAVIV3ChbaaTTGmcSzYFFp1j0nJJT9N%2FaPRIZ%2Fk%2FG9wCMVpeUdV8F6X0Sk9FAKSjI7L%2FAp07FzAc09asUQSyddNN0IQFgsMHla0%2FLV2MCrGPjvcfBn%2BmQaJ3FEte1UzgT0tu5fc7%2Fry4ZB2hbjXNlNdumPJ%2FtKs7EjTSdk%2FsML%2BC%2B9cGOqUBYP4XpRXMswzqgQHahsjzueJqLGx7An1O%2FwtvxwlMBBDwVoNyich8UFSxTfo3X48AnfaalQjQP34vxDtGHk0q3qAhr61%2FUyvSCnC5A4NQeXNVnZTcVtVu3%2Fob3tW7%2FgwdkXe%2FBer422f%2FenIjLI1yrjqUJd87rqC3sX7zXI4rPgRt%2FK%2BzqZdSesdIbFyYurTwItqCAXr%2BeFcMgY6OIwB7hqLTtkd1&X-Amz-Signature=2b530a6298e8f76d6b469f55bfcde8b000e5f85baf5a79be58dd598fc6d0ecb7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



