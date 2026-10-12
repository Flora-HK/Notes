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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637LNP4LG%2F20261012%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261012T084231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAqHT4nnZWLrrbzpe5yy9tMFwR%2BWNV1kOjJ0MM3bgzjHAiAE2MuLnDOXx65EhI%2Bj1r%2BG6mCP6pbn1B78gutQSBRmPCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDBPrCo0ibVrCbR6%2BKtwDtjlc1tE%2B6NhNE2y9eqrxriwrrv4qfRFcl5pSnv2tCqnUJhRd15zfbWuWopPbfC7pHdvwklUkt6L6Z9w3%2Fd%2F0%2BIHxwAfajTtx9Pu1YrOwW95U1IQ5c04%2F%2Fl5rjndsANZIS9AM2i6g%2FmGQUNeRdYxgs%2FJFC8s3MDGdEouQdiM9zAZPKzSuFZdGXm2Eb%2FVpWNU%2FBCmhma3Z3HAzO1YzFmVizAM43104A771J6HO4M9zlqbtLrvcSFC%2BhCVppi1zlsDCxnjCO28IERvjxxbHcXiGQA6vqjo7%2B4r5ZUZ%2FLABnn9b1EbWy255tR1zk%2BS6OdsfWSAVY5RKuViWDfkYmiRm8CqWxKsIyx4Xt76CdK6r68I%2FsTj7BIsTtb78EHQcUBsbHAc%2BIqekOqNBUFsbMc4MgPmartX86sf3qKALujTHuXcczRLlZQztFNaogsYF6IaP3A0Rt5uLb0PmWLx484od1aZ6R6hDq0w72Rl5VSCkLzz7AJp%2FAD%2BUsmm7SMK2JIOXysZ6RNwYW4JI5PKY2fA%2FD%2BVDaelsd4jhTVvPUgu8BMxgcIlRv7rXWr4pbHB7v6JSABuodheaTzBsEI1a2LgskUY9jnbQ%2BFsONFE3NRk1w43kqKNIJD8rjwBlB2vww17Gy1gY6pgF6mTK%2ByDJSlWoH48wfVwKkrGZptmk6L%2FoDhAgW670awXaNqXDEp5%2Fh1ks5cNbAwz04Pf33Usoc3uu8p9C%2BtL2TSbFv9%2F2GUrNz7sNAeU%2FTox%2F0cYmpxKqBL3wo87MCi9I4YstzM9C3urc6iLdAKLzEfSOlIqyW2bZXsmDtdUeKOgW5IZs1599rjqxmTmf33rzzuNcWgiAyStxYTzGuBMAUt3tlm1Qp&X-Amz-Signature=e737c5ed8cc118b3e6b689752b1ea9c677f6e5a8c0dd9e540df1196860f83d9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637LNP4LG%2F20261012%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261012T084231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAqHT4nnZWLrrbzpe5yy9tMFwR%2BWNV1kOjJ0MM3bgzjHAiAE2MuLnDOXx65EhI%2Bj1r%2BG6mCP6pbn1B78gutQSBRmPCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDBPrCo0ibVrCbR6%2BKtwDtjlc1tE%2B6NhNE2y9eqrxriwrrv4qfRFcl5pSnv2tCqnUJhRd15zfbWuWopPbfC7pHdvwklUkt6L6Z9w3%2Fd%2F0%2BIHxwAfajTtx9Pu1YrOwW95U1IQ5c04%2F%2Fl5rjndsANZIS9AM2i6g%2FmGQUNeRdYxgs%2FJFC8s3MDGdEouQdiM9zAZPKzSuFZdGXm2Eb%2FVpWNU%2FBCmhma3Z3HAzO1YzFmVizAM43104A771J6HO4M9zlqbtLrvcSFC%2BhCVppi1zlsDCxnjCO28IERvjxxbHcXiGQA6vqjo7%2B4r5ZUZ%2FLABnn9b1EbWy255tR1zk%2BS6OdsfWSAVY5RKuViWDfkYmiRm8CqWxKsIyx4Xt76CdK6r68I%2FsTj7BIsTtb78EHQcUBsbHAc%2BIqekOqNBUFsbMc4MgPmartX86sf3qKALujTHuXcczRLlZQztFNaogsYF6IaP3A0Rt5uLb0PmWLx484od1aZ6R6hDq0w72Rl5VSCkLzz7AJp%2FAD%2BUsmm7SMK2JIOXysZ6RNwYW4JI5PKY2fA%2FD%2BVDaelsd4jhTVvPUgu8BMxgcIlRv7rXWr4pbHB7v6JSABuodheaTzBsEI1a2LgskUY9jnbQ%2BFsONFE3NRk1w43kqKNIJD8rjwBlB2vww17Gy1gY6pgF6mTK%2ByDJSlWoH48wfVwKkrGZptmk6L%2FoDhAgW670awXaNqXDEp5%2Fh1ks5cNbAwz04Pf33Usoc3uu8p9C%2BtL2TSbFv9%2F2GUrNz7sNAeU%2FTox%2F0cYmpxKqBL3wo87MCi9I4YstzM9C3urc6iLdAKLzEfSOlIqyW2bZXsmDtdUeKOgW5IZs1599rjqxmTmf33rzzuNcWgiAyStxYTzGuBMAUt3tlm1Qp&X-Amz-Signature=efca2178e324df670f3a749e42afc97302abff6d6c069ce53c4c9158b1624f91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



