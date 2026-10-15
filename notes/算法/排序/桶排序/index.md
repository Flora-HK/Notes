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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6NNC4UY%2F20261015%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261015T070144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnvIxMuCp2aelKL49eEbGPePNAJzkDFr0LDsodjEZshAiBSRzfdX%2BbILjf6aANXBeFqJ%2Bnf41IJq0dwZFX6%2FfXj2yqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BkS8Exk7RPyujSqGKtwDXzAXCqx2XEWa32NCT5o9YeCxLX%2FFFS38MKzEv2YjWW1uuRESs0UHiV9AqqbzphPgAFIWa0Xb2sBLeNgsvUhNH97zELu8duFz40W8p9RRuqxMVfiiAMG9unxHbo0AROEZHPLaErmboJuHNElsGKewM7jdkZ4rsUX1Xe8od%2F8buRe3ueV2hsCbV%2BIMph9P0HSxgV%2FN58ZFK7lPAXS6p4xROxOv8jMYcIfz%2F8OzUXdKjl42grJXgItQ5Dq02qSiDrH6Z%2FvhnGn5N0P79AbLp6fGQePFw81USqWdep22uk2QKarjCrbbUQWAa4clPoTuo%2Fw6da%2BBgcwGWMchKgHDxhtXwpzgi09To2RdzNYRBIJYcqPnTS%2FE3yXzPDYMJG9%2BYtOwgOYSfZoCBAYWxJmiHg%2FcumaDdxStBlelT4NUZ3WoiNktQsokDRETUZaU%2FODiH6BtNekjSO5lrbAvVbblhrbrvCPbYWUX%2FbWMs5h5XzXFZ1FUkWV7NhfBxTwyB%2Bg1iYKO%2BMm%2FQPHGPqY%2FILLlDwzBlwX4wotklL18gE9HvbNYCd4Rah9Bp0l%2FNBjAP13w3a62b9HnD4wbNLG3v3sDvZUeFLGhfBWb1hIlG%2FAKh%2FhC2uXUghT9t3QGR3eUz8wwudPB1gY6pgEEZlcjThfE40%2FjoPTx6gVYxbubnC7uxXOFf%2BALmNJ1QfWJnShNUGqn6gPwdpwBDSKexGRPCb2uEv1wN%2BX4bLs0i2TcSN20ejgHX9HQ1iVrPJw8a710JzEOtqgIeyd2uT2bB25e%2BNqTcEFbxeXcbnHIx4F%2Fa0n0gu1pvqMGOGnqGaNmr%2BmmsnN1Fpt8AM4RctI7ec3fG2DEstmkfOVab%2B9OXix4QNq%2B&X-Amz-Signature=7d4780c50f9a746e9524fda3f6459e426b7f17e7ddc6a8c3e728bc1e65973736&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6NNC4UY%2F20261015%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261015T070144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnvIxMuCp2aelKL49eEbGPePNAJzkDFr0LDsodjEZshAiBSRzfdX%2BbILjf6aANXBeFqJ%2Bnf41IJq0dwZFX6%2FfXj2yqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BkS8Exk7RPyujSqGKtwDXzAXCqx2XEWa32NCT5o9YeCxLX%2FFFS38MKzEv2YjWW1uuRESs0UHiV9AqqbzphPgAFIWa0Xb2sBLeNgsvUhNH97zELu8duFz40W8p9RRuqxMVfiiAMG9unxHbo0AROEZHPLaErmboJuHNElsGKewM7jdkZ4rsUX1Xe8od%2F8buRe3ueV2hsCbV%2BIMph9P0HSxgV%2FN58ZFK7lPAXS6p4xROxOv8jMYcIfz%2F8OzUXdKjl42grJXgItQ5Dq02qSiDrH6Z%2FvhnGn5N0P79AbLp6fGQePFw81USqWdep22uk2QKarjCrbbUQWAa4clPoTuo%2Fw6da%2BBgcwGWMchKgHDxhtXwpzgi09To2RdzNYRBIJYcqPnTS%2FE3yXzPDYMJG9%2BYtOwgOYSfZoCBAYWxJmiHg%2FcumaDdxStBlelT4NUZ3WoiNktQsokDRETUZaU%2FODiH6BtNekjSO5lrbAvVbblhrbrvCPbYWUX%2FbWMs5h5XzXFZ1FUkWV7NhfBxTwyB%2Bg1iYKO%2BMm%2FQPHGPqY%2FILLlDwzBlwX4wotklL18gE9HvbNYCd4Rah9Bp0l%2FNBjAP13w3a62b9HnD4wbNLG3v3sDvZUeFLGhfBWb1hIlG%2FAKh%2FhC2uXUghT9t3QGR3eUz8wwudPB1gY6pgEEZlcjThfE40%2FjoPTx6gVYxbubnC7uxXOFf%2BALmNJ1QfWJnShNUGqn6gPwdpwBDSKexGRPCb2uEv1wN%2BX4bLs0i2TcSN20ejgHX9HQ1iVrPJw8a710JzEOtqgIeyd2uT2bB25e%2BNqTcEFbxeXcbnHIx4F%2Fa0n0gu1pvqMGOGnqGaNmr%2BmmsnN1Fpt8AM4RctI7ec3fG2DEstmkfOVab%2B9OXix4QNq%2B&X-Amz-Signature=9c53e12365b33eab9b44b2c119d72a9b3b443b1dbf50d9c525801a566cdb4468&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



