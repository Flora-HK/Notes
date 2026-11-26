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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PMZSQW3%2F20261126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261126T103015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCjXthkLGdx9X8yM0bte8KBKHe64pO6cwEw8aDxPaT%2BwIhAMw%2B1%2BIGkWaH6qYi0XICExoEekkEafLFH%2B59wosZergBKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwg1vgmKuiV9RnptcYq3AN8fTRGhUA8myVez9hXWMWNV8%2F5kzN597RTlM0rnvrN9LRcaDVXuC6bR2P%2F%2FhdXU6XjAT8AGMlokY%2BwNcf2LuG9qN4QniHlMFuf0pn1JVwJBHs%2FOBu8gF4s52zk%2F9VnflNnWtL9WF1mb2T3TjTBeIN0L6mW4iWobi3ImKwVaFr97Kg%2B5AzTzBr67Y3XoYqWJiaY9HBE5qCBBaXuZzQr9%2BHiCanPntHmlm6LyYwdPqeuY8uMaskSQm0p0y60YInQYQBIklU8UMJe%2BxXdH08tk5CG4kCkPgpr3LISQNlOWTd6eZ3Cj9KD97XbV6bnt7pz5wbzRpTfY5CbCcx3t2YJXMnj6SBCaGR9HIGGuul7u%2FwwYuH6S4ep93PnlY6If6j04%2BT19MRhElmJO6wH3OV0FxuvfzjSAiR%2BZIjQpG29mjhPD9ZfiQEGfPxoa9e8W7wYUtBNL4Bm7fK16harM82QR3PXIiYsdA38haIBKzyc54w9Kil4iqAhhpRhucDqROfdcdwWunW2V%2B3UUAULVNRFbNBhJc6XJP%2B5I%2BCPWKEAlRMHrQRrMxBJvJQfW5xm6pLMUI%2FslMx3prc8TqobnkvBbKEN5CX3xWCwuHMkgFlyi%2FG3OqtLvYhL5AEz2BVZmDCWg6DYBjqkAUEUT6OvSK7McK0t%2BeDGs8sMU%2FPqYeR3l%2B6mqaBs7UoK8Kc6g%2Fn%2BSikLOsm42hwcCF8YC3QmTrmZJTiAVezYxsNhmaimWEI3nD2%2BV1JVuxUYiVojkBYnJtTyePi8t16KQoPcV1Rgp6hmUdk3iprlI%2BvAY1PIbBKwYoeEgYTW0XhcbtrfD24%2Ff0Ea0zUazwX5GxDfMQJ9qwey1nNvLxreIk4%2FQQ2V&X-Amz-Signature=21b3699ee464e81b69e47ed48bdeca4195c79ef987c566a2a4215e07de976d05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PMZSQW3%2F20261126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261126T103015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCjXthkLGdx9X8yM0bte8KBKHe64pO6cwEw8aDxPaT%2BwIhAMw%2B1%2BIGkWaH6qYi0XICExoEekkEafLFH%2B59wosZergBKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwg1vgmKuiV9RnptcYq3AN8fTRGhUA8myVez9hXWMWNV8%2F5kzN597RTlM0rnvrN9LRcaDVXuC6bR2P%2F%2FhdXU6XjAT8AGMlokY%2BwNcf2LuG9qN4QniHlMFuf0pn1JVwJBHs%2FOBu8gF4s52zk%2F9VnflNnWtL9WF1mb2T3TjTBeIN0L6mW4iWobi3ImKwVaFr97Kg%2B5AzTzBr67Y3XoYqWJiaY9HBE5qCBBaXuZzQr9%2BHiCanPntHmlm6LyYwdPqeuY8uMaskSQm0p0y60YInQYQBIklU8UMJe%2BxXdH08tk5CG4kCkPgpr3LISQNlOWTd6eZ3Cj9KD97XbV6bnt7pz5wbzRpTfY5CbCcx3t2YJXMnj6SBCaGR9HIGGuul7u%2FwwYuH6S4ep93PnlY6If6j04%2BT19MRhElmJO6wH3OV0FxuvfzjSAiR%2BZIjQpG29mjhPD9ZfiQEGfPxoa9e8W7wYUtBNL4Bm7fK16harM82QR3PXIiYsdA38haIBKzyc54w9Kil4iqAhhpRhucDqROfdcdwWunW2V%2B3UUAULVNRFbNBhJc6XJP%2B5I%2BCPWKEAlRMHrQRrMxBJvJQfW5xm6pLMUI%2FslMx3prc8TqobnkvBbKEN5CX3xWCwuHMkgFlyi%2FG3OqtLvYhL5AEz2BVZmDCWg6DYBjqkAUEUT6OvSK7McK0t%2BeDGs8sMU%2FPqYeR3l%2B6mqaBs7UoK8Kc6g%2Fn%2BSikLOsm42hwcCF8YC3QmTrmZJTiAVezYxsNhmaimWEI3nD2%2BV1JVuxUYiVojkBYnJtTyePi8t16KQoPcV1Rgp6hmUdk3iprlI%2BvAY1PIbBKwYoeEgYTW0XhcbtrfD24%2Ff0Ea0zUazwX5GxDfMQJ9qwey1nNvLxreIk4%2FQQ2V&X-Amz-Signature=629d252470a26679d6fc0332426e31a018df3baa0e8fa81b0f88ac70747b4a6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



