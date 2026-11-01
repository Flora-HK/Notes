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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AZPMSBJ%2F20261101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261101T084756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGTwOTmNJZvU1lE5bybuK2wj5reajaLR7bZg7%2Fd8zs4ZAiA3ypN4mx6ToWMZYRmy7gU3FAiHeP4%2BLzlKZe4kLhJ1bCr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMIS2yym60WXF0XbNxKtwDvIzM5I%2FRjD19Ks%2BJ7v%2BidAgMS9SFbLXp%2FJss2altr8lhymXsSoAFLLz7XvMdWUz8989Aa6Y3RsIfwcO7Dui1U4SpuBY8Y%2B%2FYy88cmxa71hsKoXyEzr%2FtO1vDGvXZR6Zb5HEX0vzf%2B19wpo3FAWQ%2FVYkNV%2FCNIFCeZVt6BUuMHDj%2BNwRhxsYMmYNvnVuhA4M%2FtICZhaZwhRmRzPxx1UAV%2B4lAFDa1h5Na5%2F%2BZrHT70kj41q1U8C%2Fmd7%2BRR58flUIcHRKh%2F6609GX%2FA3khzG6lC0uaVQhBQud%2BrfCrsYAiaaaxix4MOJc8w8H8wpsWO2AicsJmdMrPw1qZvyu6rFYkU8MVVKuh1ErTsEb8UHI4%2Bhlxbq2NYUMFqH5kkhzNEMCqiwzKAbxEeW9bqnHFDb0YqbzarNe1zLTGuiRdlPgbyrC6hPvahuB0F53SG7E%2F0TKoJQqg0H%2Ft%2BzQUPM1QT8gTw0kSzM4NQnh4uP31s9HXIGLPrtgXW7Ca7GaZYFNzqwuGf6T%2FBHjspIH5BEEP1IcwaRHopz5NWexHxJRL2NOP0EjCp25Z4jJXZR8MSoG3HFmKq3OwNmNuGmbhoOx3M06TI%2FMQGLv65ocHkg%2BWQh41%2B2t4HnACe1CbTmRlDW8wmNub1wY6pgFpLcX%2FKYUjmJ9EdU%2FpWa8Lw9PZLsDAVilqw5TvWzteu8vJknZx1i0xVlH6xAcDOxqrpz2zxEVUbU8fIEEQg4sVinZC9Mq1FEjht0jMzAO37IQWDq73KmARmNBjfkOJHo7%2B74JOQisFnWkQL5BP7iUGfBsoq9kvk3665c8qVEqItjueE2MREpaPtQBFMGG5%2Fr45AewLBs8Ck2ouEQjzxLEMjCk6WxjQ&X-Amz-Signature=e65a11da3445ba9d1225081187f120edc0ad02b2455bd87ccee5d8fad70a8666&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AZPMSBJ%2F20261101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261101T084756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGTwOTmNJZvU1lE5bybuK2wj5reajaLR7bZg7%2Fd8zs4ZAiA3ypN4mx6ToWMZYRmy7gU3FAiHeP4%2BLzlKZe4kLhJ1bCr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMIS2yym60WXF0XbNxKtwDvIzM5I%2FRjD19Ks%2BJ7v%2BidAgMS9SFbLXp%2FJss2altr8lhymXsSoAFLLz7XvMdWUz8989Aa6Y3RsIfwcO7Dui1U4SpuBY8Y%2B%2FYy88cmxa71hsKoXyEzr%2FtO1vDGvXZR6Zb5HEX0vzf%2B19wpo3FAWQ%2FVYkNV%2FCNIFCeZVt6BUuMHDj%2BNwRhxsYMmYNvnVuhA4M%2FtICZhaZwhRmRzPxx1UAV%2B4lAFDa1h5Na5%2F%2BZrHT70kj41q1U8C%2Fmd7%2BRR58flUIcHRKh%2F6609GX%2FA3khzG6lC0uaVQhBQud%2BrfCrsYAiaaaxix4MOJc8w8H8wpsWO2AicsJmdMrPw1qZvyu6rFYkU8MVVKuh1ErTsEb8UHI4%2Bhlxbq2NYUMFqH5kkhzNEMCqiwzKAbxEeW9bqnHFDb0YqbzarNe1zLTGuiRdlPgbyrC6hPvahuB0F53SG7E%2F0TKoJQqg0H%2Ft%2BzQUPM1QT8gTw0kSzM4NQnh4uP31s9HXIGLPrtgXW7Ca7GaZYFNzqwuGf6T%2FBHjspIH5BEEP1IcwaRHopz5NWexHxJRL2NOP0EjCp25Z4jJXZR8MSoG3HFmKq3OwNmNuGmbhoOx3M06TI%2FMQGLv65ocHkg%2BWQh41%2B2t4HnACe1CbTmRlDW8wmNub1wY6pgFpLcX%2FKYUjmJ9EdU%2FpWa8Lw9PZLsDAVilqw5TvWzteu8vJknZx1i0xVlH6xAcDOxqrpz2zxEVUbU8fIEEQg4sVinZC9Mq1FEjht0jMzAO37IQWDq73KmARmNBjfkOJHo7%2B74JOQisFnWkQL5BP7iUGfBsoq9kvk3665c8qVEqItjueE2MREpaPtQBFMGG5%2Fr45AewLBs8Ck2ouEQjzxLEMjCk6WxjQ&X-Amz-Signature=dd86ba13c0a0c896c42bcf70f34fc1b3013642ced13600fc3834810163cb96b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



