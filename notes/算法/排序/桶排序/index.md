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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OUNTQYT%2F20261110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261110T092051Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIBOK9CHDDjF6ik%2BvC%2BbgJ%2BWxmPCF2D%2B792y2Cp9qsbrVAiEAhHU6vUNXb%2Bfsy6RzOGezHMZFFAYMstynh%2B2Yj1tnIQoq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDPPkK9a%2B5jiojM5kqyrcA92V9dG%2FNhRs9c93advv5Gp3fqAyDkYYMrD41Rg3HgT4%2FfNHYOJXoXszZGGV5Hl%2FND7%2BK6jDPZrhHusTtuK7kxL0Yb%2B1eaDzDa09JKF6A0QnAaG30fgWSaYOL4jQJbE6sucbbUIlcjP2YUjeQX4jRG4I%2FXVuh8WPxkFKMBRSIQuYRC4WmAnk3TAkYkL9OX5fWOV75NC91DnkslO%2FuSaiRUycCEy2jnHeHaWMEO9gnObs%2FuuJUziUp93o4qOO2iuMcRFFEQxnq53kxvQuQ1yq8%2BafqqEHtffEMrBPKecxEySIHTR9aBGw3v1lk1bxfPRG2wEwArpIUMURJkxbN3%2FfKSql4F46dtcuLmeJuD%2Fw%2F39TfmgABlTaMIyQ%2FncOcwWnMe68RF6NktK%2Bqe2qTb9UNQNDEIfEXU9y8tK5fvFZosWGtzSAwcwvFX66jGmpJxSKKL2HTbs1mzFIaIAUbvbyEoKOo0UWgYZ7G2d%2BTAe8PQJWh2jP2ChM%2FhQobmHg%2F0J7hqsB2G61yq%2FWd5cwctSQnCgckL%2FbPiXj17n2KqJeeT%2BUHcsp1IVHORzmuKP4C3%2FRsuaRoKk3HVgHLoMR0tk9Fc6%2BPX0MvqL3iRfIfA7xvIDJ9Sa27QBpMez8pLCyMMDXytcGOqUBlwCRhCnDbvFGd6ycinJIkeqQgchkq4fe49EcUMYjBfN6NcvbxXtJttXBPKSw5h%2Fxl7FCpHsaznX7pW3lP5nkniBZl4PuT5UCZ9Gk4Wy7zZXH9GV4z%2FD41hkXx68j9SFdkaqGgzuLExD5gcF198YhXs8HQBHKcJs9h7kqKCz34fIX31LwU7wdu9tAernIaiXJnHwb3gpiS%2B4axl2GEa%2BITE4bGq2x&X-Amz-Signature=4da1c0c66a57a09b0cd7e8afda0bd7eefd48f2da583268ca1a408f490e75fcf0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OUNTQYT%2F20261110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261110T092051Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIBOK9CHDDjF6ik%2BvC%2BbgJ%2BWxmPCF2D%2B792y2Cp9qsbrVAiEAhHU6vUNXb%2Bfsy6RzOGezHMZFFAYMstynh%2B2Yj1tnIQoq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDPPkK9a%2B5jiojM5kqyrcA92V9dG%2FNhRs9c93advv5Gp3fqAyDkYYMrD41Rg3HgT4%2FfNHYOJXoXszZGGV5Hl%2FND7%2BK6jDPZrhHusTtuK7kxL0Yb%2B1eaDzDa09JKF6A0QnAaG30fgWSaYOL4jQJbE6sucbbUIlcjP2YUjeQX4jRG4I%2FXVuh8WPxkFKMBRSIQuYRC4WmAnk3TAkYkL9OX5fWOV75NC91DnkslO%2FuSaiRUycCEy2jnHeHaWMEO9gnObs%2FuuJUziUp93o4qOO2iuMcRFFEQxnq53kxvQuQ1yq8%2BafqqEHtffEMrBPKecxEySIHTR9aBGw3v1lk1bxfPRG2wEwArpIUMURJkxbN3%2FfKSql4F46dtcuLmeJuD%2Fw%2F39TfmgABlTaMIyQ%2FncOcwWnMe68RF6NktK%2Bqe2qTb9UNQNDEIfEXU9y8tK5fvFZosWGtzSAwcwvFX66jGmpJxSKKL2HTbs1mzFIaIAUbvbyEoKOo0UWgYZ7G2d%2BTAe8PQJWh2jP2ChM%2FhQobmHg%2F0J7hqsB2G61yq%2FWd5cwctSQnCgckL%2FbPiXj17n2KqJeeT%2BUHcsp1IVHORzmuKP4C3%2FRsuaRoKk3HVgHLoMR0tk9Fc6%2BPX0MvqL3iRfIfA7xvIDJ9Sa27QBpMez8pLCyMMDXytcGOqUBlwCRhCnDbvFGd6ycinJIkeqQgchkq4fe49EcUMYjBfN6NcvbxXtJttXBPKSw5h%2Fxl7FCpHsaznX7pW3lP5nkniBZl4PuT5UCZ9Gk4Wy7zZXH9GV4z%2FD41hkXx68j9SFdkaqGgzuLExD5gcF198YhXs8HQBHKcJs9h7kqKCz34fIX31LwU7wdu9tAernIaiXJnHwb3gpiS%2B4axl2GEa%2BITE4bGq2x&X-Amz-Signature=3f41e4961de9d5744a1af215a4fdd32f5244cd063f62dc54c0f6fb1c6e26fb6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



