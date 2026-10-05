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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZMAZLJV%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T082731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLXdlc3QtMiJHMEUCIQCDF%2FB%2FZemCzYJRt3xzATJAKO51tB9IjjUwDkUE723nHAIgMs7sHKjKylIETAagg7kqd3fu6mVOGwl%2BQF5IQ%2BUvG2EqiAQI2P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC6o4H1IcDxrBvBXrCrcA9x4pWITZyafGKoZtMm16HSSMcveME6I1g%2Fyin1eRvIY8BEmPbh2E1InYcyS9EABYz0iXj%2BtgVSdHQq43nDAUeFFO1O3vNE9ojF89uxo7oaGJyO7oRHLvvsm4BVdH1ZIAqCt6mq28XVidRFz4oluPJkknk%2Bs5VUKKDqMjuVm5EjFqV2lKgL0jyyHiHC9wLuXZ1tXgvG7sJLdYvFFvXxuaY%2BkB5Yh60s2lwg%2FwOCX6ekoBnx2wtPdX4teMMJvtDx4ImtuSZL9VDiRgdTBEUgGT6BkUU9WFtT7tX0OKwz4GlrUbnlFlLvZE5kmRUqdtd4hgqFFaB7uDYwjxy8V26ymoOrD3E%2BMelB9aMA7l1fNyNUZ%2BpqS0EIwDZrJosK5%2FKbhEAqewS5%2FXRLh2gosJFBZkUuaF6mw81IKC25Ne%2FNfDSPPwYsHc21MiP8LO9TBFaBMnRjq%2Fvw%2BWL7tyLXDAVt3lprvjnf8zFD8HaxduXYHRZ5cEV%2B61s%2FHGfcZBnkMVfRCDs8tke1vLRne7kLBTQAEuiAtQ%2Bh1ks1wTH9VfKrWkxEnccHInZFhwc4CtQX1h7FF3ghmzmtlHZkOL5%2BxJ%2FjjX1Es5yXcPDxhDQ9FakMoEdnMU4gHd4ZNVdifj4wtMPWZjdYGOqUBTPXax9TlP3Jjst3T5B4vtsgVHuBwV3KoF9AAz4eZDuhmcNVzmQSW%2BN4vSMHi1u9XvCaV7JgbNwSNawn0HngvUoW1uqBZOL%2FEU36cdiS3TBculeEKx64L4Z3GGEw4EDsm3XnUq2RHLZUSp2EF0SHxZt1NBOuoEsf71f5XxjaG%2BoICpE0QDvz7DmAvkRnJAZD7oXR3gHT1Bt5SLgdmSZp2aE82yjYG&X-Amz-Signature=8a707a9c79db377be6f7084c12c045df1d1b476bbb3aa8b48207489ae83233e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZMAZLJV%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T082731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLXdlc3QtMiJHMEUCIQCDF%2FB%2FZemCzYJRt3xzATJAKO51tB9IjjUwDkUE723nHAIgMs7sHKjKylIETAagg7kqd3fu6mVOGwl%2BQF5IQ%2BUvG2EqiAQI2P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC6o4H1IcDxrBvBXrCrcA9x4pWITZyafGKoZtMm16HSSMcveME6I1g%2Fyin1eRvIY8BEmPbh2E1InYcyS9EABYz0iXj%2BtgVSdHQq43nDAUeFFO1O3vNE9ojF89uxo7oaGJyO7oRHLvvsm4BVdH1ZIAqCt6mq28XVidRFz4oluPJkknk%2Bs5VUKKDqMjuVm5EjFqV2lKgL0jyyHiHC9wLuXZ1tXgvG7sJLdYvFFvXxuaY%2BkB5Yh60s2lwg%2FwOCX6ekoBnx2wtPdX4teMMJvtDx4ImtuSZL9VDiRgdTBEUgGT6BkUU9WFtT7tX0OKwz4GlrUbnlFlLvZE5kmRUqdtd4hgqFFaB7uDYwjxy8V26ymoOrD3E%2BMelB9aMA7l1fNyNUZ%2BpqS0EIwDZrJosK5%2FKbhEAqewS5%2FXRLh2gosJFBZkUuaF6mw81IKC25Ne%2FNfDSPPwYsHc21MiP8LO9TBFaBMnRjq%2Fvw%2BWL7tyLXDAVt3lprvjnf8zFD8HaxduXYHRZ5cEV%2B61s%2FHGfcZBnkMVfRCDs8tke1vLRne7kLBTQAEuiAtQ%2Bh1ks1wTH9VfKrWkxEnccHInZFhwc4CtQX1h7FF3ghmzmtlHZkOL5%2BxJ%2FjjX1Es5yXcPDxhDQ9FakMoEdnMU4gHd4ZNVdifj4wtMPWZjdYGOqUBTPXax9TlP3Jjst3T5B4vtsgVHuBwV3KoF9AAz4eZDuhmcNVzmQSW%2BN4vSMHi1u9XvCaV7JgbNwSNawn0HngvUoW1uqBZOL%2FEU36cdiS3TBculeEKx64L4Z3GGEw4EDsm3XnUq2RHLZUSp2EF0SHxZt1NBOuoEsf71f5XxjaG%2BoICpE0QDvz7DmAvkRnJAZD7oXR3gHT1Bt5SLgdmSZp2aE82yjYG&X-Amz-Signature=8855e5aff7055ae1fead1cdf80eac73c133edb46bc61435027f52f8b0b7ac17b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



