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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZZPCVKL%2F20261023%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261023T070219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCL0eBddYchY5vuw31teoo6QrczQw80wzKZQg6Wp2GpxAIgSGMPO8HXiEavObmu44nIiUbLvoe%2Fmb2snTCKj2nskc0qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLP5emXlMpq5lrNuLyrcA6d6HbxoQUJuLNQxIkWWJqdS%2BXvRCSUa9Tv0Xzz0K1ynE8YwtsiqIsJzSwezFnK%2B66Z4rTWIO4feMX6Mn0%2F2n6eES3DGp%2Brg7s25nWOodlOgTdIImy9Y9y0z%2BIDbNHvPmH5mIovv0U95SE9d%2BR619qJ0LcOIpXQoEQhw3bvE7KwrU6IwGeZbm333nCzE6k9BPan%2B2ivkW1hLsOZw%2FztYdJmGAsrWpewGrkhvRpUjWB8%2Fuo9REGmAopMvEHZW5VQH4s8qIdQmi5SGZF8Auq0qf2twa0O9%2Fj1D%2Fkj5MLvB%2FhsruAt61zinl3hl2GAFQfEHR9QdRUBuvu7aSvdDrICJJgDQPWtzsRhVFlb0eqA%2F5X%2F6JakIandn%2BkbV%2BA4X2aIMeRzfld0IPCaaVHqP3mScBPWzBRCrw8VqUNLniVl14BfXCG4iuUUjuM%2Bl3jN1fM3APHFkDHs%2F3K6PR2Z8fQiocB0tk5U19Snk74oMR65belUNiJAKe20yswCI%2BWAd%2BX4xrKXtBPK57sRvGr%2FAOHFy6431BPL8AfOh4z0HoW%2FW08lauU%2FaX7zc9my2HCT0PcJjOtq7J0pXxgr%2B5LdFs8qvtlFE123cr8E%2FkDRwL1CjPvhfo8KRfVT3HFV4YM%2FnMLGG69YGOqUBmjFzGsMMuvS6Nsv%2BO9s3QMOrCa9hBSZ3jod1T%2FvLKBaVFue%2FnWeTqzhk52c1BbO7k8wtsBQTxNpOZ3%2Fe9VtqJ26qp%2Bwa3twJljGxrASpWQCCUUlyOptzh8kSGp%2FMo6owIAqSka9KuRz6SHjQqYc3PAdMg%2BxDF8E8zUTUjOG5qr%2FZ2lz5QKf5oZvn9E6hApMm4fOkCOOyviB2S314%2FgYo7Vp9J7cJ&X-Amz-Signature=ef1336999eb3f10b8ba81ce10494a99e736c48f5ed729fdefe5793bae231ff4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZZPCVKL%2F20261023%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261023T070219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCL0eBddYchY5vuw31teoo6QrczQw80wzKZQg6Wp2GpxAIgSGMPO8HXiEavObmu44nIiUbLvoe%2Fmb2snTCKj2nskc0qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLP5emXlMpq5lrNuLyrcA6d6HbxoQUJuLNQxIkWWJqdS%2BXvRCSUa9Tv0Xzz0K1ynE8YwtsiqIsJzSwezFnK%2B66Z4rTWIO4feMX6Mn0%2F2n6eES3DGp%2Brg7s25nWOodlOgTdIImy9Y9y0z%2BIDbNHvPmH5mIovv0U95SE9d%2BR619qJ0LcOIpXQoEQhw3bvE7KwrU6IwGeZbm333nCzE6k9BPan%2B2ivkW1hLsOZw%2FztYdJmGAsrWpewGrkhvRpUjWB8%2Fuo9REGmAopMvEHZW5VQH4s8qIdQmi5SGZF8Auq0qf2twa0O9%2Fj1D%2Fkj5MLvB%2FhsruAt61zinl3hl2GAFQfEHR9QdRUBuvu7aSvdDrICJJgDQPWtzsRhVFlb0eqA%2F5X%2F6JakIandn%2BkbV%2BA4X2aIMeRzfld0IPCaaVHqP3mScBPWzBRCrw8VqUNLniVl14BfXCG4iuUUjuM%2Bl3jN1fM3APHFkDHs%2F3K6PR2Z8fQiocB0tk5U19Snk74oMR65belUNiJAKe20yswCI%2BWAd%2BX4xrKXtBPK57sRvGr%2FAOHFy6431BPL8AfOh4z0HoW%2FW08lauU%2FaX7zc9my2HCT0PcJjOtq7J0pXxgr%2B5LdFs8qvtlFE123cr8E%2FkDRwL1CjPvhfo8KRfVT3HFV4YM%2FnMLGG69YGOqUBmjFzGsMMuvS6Nsv%2BO9s3QMOrCa9hBSZ3jod1T%2FvLKBaVFue%2FnWeTqzhk52c1BbO7k8wtsBQTxNpOZ3%2Fe9VtqJ26qp%2Bwa3twJljGxrASpWQCCUUlyOptzh8kSGp%2FMo6owIAqSka9KuRz6SHjQqYc3PAdMg%2BxDF8E8zUTUjOG5qr%2FZ2lz5QKf5oZvn9E6hApMm4fOkCOOyviB2S314%2FgYo7Vp9J7cJ&X-Amz-Signature=055606d65a1818e02de5a93322311c09f3fc6f41952e5fa2d2dcb556dd77aa86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



