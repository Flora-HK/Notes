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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJEEGERG%2F20260929%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260929T075628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQChX%2FwaiO3AMXXQfiGQD0kEcqmVE84ROMVNSsM0YiPnzwIgXrA7rXAxmmGMyX1CuMwZ2No7Vq8zA1gqnbfHj4mQSH4q%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDCRsVCMDL3%2FFQiUcwircAxTwtEImCXOBlLdPIbmrfzlMYP2%2BN%2FngU1ZVq0i0HX1R9jvqdl1AVi9drKzSxcabsvHUOMn4RwrxhuQM9hvcZYH%2FlD8owDHmS4PJW6fZ8GpSx31On%2FpWbCKxEHttphdUla4RPAJOntzB7Q4PhLjJeBM%2BnsEis%2BLbqpnLkX1ZL2b33oJgfky%2FoSFrmM4ZhXnOrMauIItXlpWUOlgik1HNusMTnEq4kif9eZbgdaYhqfTwqKKmKlHlcR%2FS2KVAc%2F16xA4ipE1lRq21rPOJvjifPqRN9nPf51X27dCiOMaRJnczVqZojoM%2BXCqJ26OO6v0%2FSMZWCLRC%2FiFfFgqgEWf9Yst8yN%2FEKgQxD%2FL7TGNLRIoeIOJiYTiEZhkLUZoyLnMMtlS5%2BEI28u%2FuIdZyMmya0DNFILkXeqMySRxjHgt3VCBs28A7IzB0LR4YCQkGO3L0b15m1Td2aU%2BOtus%2BRzRSSjUMuiM%2BRwKjcJ5xwI1HeW1TdaUsdgfRn%2FLWz9B2R7JB72wnGXmXvYMRfloRVtRLWJJMK0tZ%2FTWbWJRpyaQPXH99wmeUliPMET3OXrZ4Ja%2F81dUrnDJO16aVyjejYWqTR5XjfSp2NIDTJgZgt70hUdtRMjhNcMYpH%2FK28%2FtnMN7E7dUGOqUBLHOqS3SwC1xLbFvzfSVjCbrlvFIG6sb3qJUzouklUV3oScv63UfPFtTsHM1mmWLufVcRjFX19W3F%2BWh5P2Fs89L7m5I2itJfkMBDGVXuo%2B3WNz2Z%2FqU1Yo0Zz5aYqE4Sp5ZIJT1GIHEyG8YlG5YZf6zlurlXrdmooLNUTqPc%2FVCHC0WK%2Fr164FAQ4ofkP06gYH%2FSs9HdaD3l%2FRHz4pnMxQQ8fKl9&X-Amz-Signature=7cd3672124bd63c89e1ab69db149e8e75702b5ac4e3bc2ffc446729edd15733b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJEEGERG%2F20260929%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260929T075628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQChX%2FwaiO3AMXXQfiGQD0kEcqmVE84ROMVNSsM0YiPnzwIgXrA7rXAxmmGMyX1CuMwZ2No7Vq8zA1gqnbfHj4mQSH4q%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDCRsVCMDL3%2FFQiUcwircAxTwtEImCXOBlLdPIbmrfzlMYP2%2BN%2FngU1ZVq0i0HX1R9jvqdl1AVi9drKzSxcabsvHUOMn4RwrxhuQM9hvcZYH%2FlD8owDHmS4PJW6fZ8GpSx31On%2FpWbCKxEHttphdUla4RPAJOntzB7Q4PhLjJeBM%2BnsEis%2BLbqpnLkX1ZL2b33oJgfky%2FoSFrmM4ZhXnOrMauIItXlpWUOlgik1HNusMTnEq4kif9eZbgdaYhqfTwqKKmKlHlcR%2FS2KVAc%2F16xA4ipE1lRq21rPOJvjifPqRN9nPf51X27dCiOMaRJnczVqZojoM%2BXCqJ26OO6v0%2FSMZWCLRC%2FiFfFgqgEWf9Yst8yN%2FEKgQxD%2FL7TGNLRIoeIOJiYTiEZhkLUZoyLnMMtlS5%2BEI28u%2FuIdZyMmya0DNFILkXeqMySRxjHgt3VCBs28A7IzB0LR4YCQkGO3L0b15m1Td2aU%2BOtus%2BRzRSSjUMuiM%2BRwKjcJ5xwI1HeW1TdaUsdgfRn%2FLWz9B2R7JB72wnGXmXvYMRfloRVtRLWJJMK0tZ%2FTWbWJRpyaQPXH99wmeUliPMET3OXrZ4Ja%2F81dUrnDJO16aVyjejYWqTR5XjfSp2NIDTJgZgt70hUdtRMjhNcMYpH%2FK28%2FtnMN7E7dUGOqUBLHOqS3SwC1xLbFvzfSVjCbrlvFIG6sb3qJUzouklUV3oScv63UfPFtTsHM1mmWLufVcRjFX19W3F%2BWh5P2Fs89L7m5I2itJfkMBDGVXuo%2B3WNz2Z%2FqU1Yo0Zz5aYqE4Sp5ZIJT1GIHEyG8YlG5YZf6zlurlXrdmooLNUTqPc%2FVCHC0WK%2Fr164FAQ4ofkP06gYH%2FSs9HdaD3l%2FRHz4pnMxQQ8fKl9&X-Amz-Signature=7ac5a0bf583007713c2fa92b9164a063d5fd8f8ea40fdd8f1769db8a8c7b1bbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



