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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFNVFQXG%2F20261106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261106T085753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQCOKGUGjVAHDzCUvnTzs3Zk9%2B7GbFhbt6ZroMNOHpvufAIhANe5qanKUY4Tq%2FugJdbZ0i%2B3C8o8mlCT%2BRUSHP7kqnK6KogECNn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyLR2I%2FBzwKJ9vvwk0q3APu7gfETho4XXD5%2FOf2PQS25Cd3vMKGm9HPGVzR8OhMrnQwYyNn2WoTzrXnc8m%2FM32vvKd%2Bk%2FWgFlD1OEVDVzESjNDatY4bwPapBiVqcBhA8NHufEQ0Ocy6MIgqpkzVRYBAVUeSFxU1Pz4f7cqm4DyfLnDIuS2J93nH79BLWX9%2FzyXwHh9pv2VTDC8RRZ0dqsHxql8qyHdEw%2BIrIXff5GW2l%2FL6iGXSduO4aIUr56dk%2FIfPMhZBxOE4voMuyGHuBnERUInF3Nz6WgnlC4rz0FQKzbBdX6%2B%2BICkjZGx8u9DUjLCmUOqYNBZ%2FEevPuzCtZdsesVch0govWyG3Q7%2BqhvnljzQC%2B%2FDb4u0L%2BMgCfWKJWXH7jhc6h%2BQDE1l3RnkumacG3MseoMyK2e4JnuIM7gcqNvvLjN1f6tntjWsAZWzS4PmwZgSUMxPbWAI3p7NtlmzXD1CsfYa3KCB9%2F5XdvCbcDDVs8dyNz1aWNHFCz19IQxN7m4bh94iDW%2F3PAXTYtLPkDWk7XjcXMhJrdzWrLVEUx5bFIJsoT4GEhuwYhfWEz8ddz7CLQpkT8KG%2FqQszVPz3qHu1fHiNMzVf9iJd3hHu4SL3axNde0%2Bh9Um9fJmKn5yC0LgFNMA8g15wwzDelLbXBjqkAXCE5yav0DT4Qc%2BKe2PvAfE8uhrKm1KpMH1CKvrmFjsCzht%2BGiDH3Cose6pGl%2BoquvlcUY7vz6RkdYH1bspBMmyScqjNut16KOBsIi0k7ySqtLutaROu9V1lrs%2FjJ3Me%2BkIfvhwDRbEb75Ix5tZi66cW2Xa4a0lEFZM2Qd3LjDd20rDDS7BgH2keOVK9tnuJ6z878yQ8y60tp%2B8jvzQ1EvJXDOWl&X-Amz-Signature=fa48d35d7a035d1675f51255cf027d9833650e060fafd9073e82fe2c0a8eff72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFNVFQXG%2F20261106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261106T085753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQCOKGUGjVAHDzCUvnTzs3Zk9%2B7GbFhbt6ZroMNOHpvufAIhANe5qanKUY4Tq%2FugJdbZ0i%2B3C8o8mlCT%2BRUSHP7kqnK6KogECNn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyLR2I%2FBzwKJ9vvwk0q3APu7gfETho4XXD5%2FOf2PQS25Cd3vMKGm9HPGVzR8OhMrnQwYyNn2WoTzrXnc8m%2FM32vvKd%2Bk%2FWgFlD1OEVDVzESjNDatY4bwPapBiVqcBhA8NHufEQ0Ocy6MIgqpkzVRYBAVUeSFxU1Pz4f7cqm4DyfLnDIuS2J93nH79BLWX9%2FzyXwHh9pv2VTDC8RRZ0dqsHxql8qyHdEw%2BIrIXff5GW2l%2FL6iGXSduO4aIUr56dk%2FIfPMhZBxOE4voMuyGHuBnERUInF3Nz6WgnlC4rz0FQKzbBdX6%2B%2BICkjZGx8u9DUjLCmUOqYNBZ%2FEevPuzCtZdsesVch0govWyG3Q7%2BqhvnljzQC%2B%2FDb4u0L%2BMgCfWKJWXH7jhc6h%2BQDE1l3RnkumacG3MseoMyK2e4JnuIM7gcqNvvLjN1f6tntjWsAZWzS4PmwZgSUMxPbWAI3p7NtlmzXD1CsfYa3KCB9%2F5XdvCbcDDVs8dyNz1aWNHFCz19IQxN7m4bh94iDW%2F3PAXTYtLPkDWk7XjcXMhJrdzWrLVEUx5bFIJsoT4GEhuwYhfWEz8ddz7CLQpkT8KG%2FqQszVPz3qHu1fHiNMzVf9iJd3hHu4SL3axNde0%2Bh9Um9fJmKn5yC0LgFNMA8g15wwzDelLbXBjqkAXCE5yav0DT4Qc%2BKe2PvAfE8uhrKm1KpMH1CKvrmFjsCzht%2BGiDH3Cose6pGl%2BoquvlcUY7vz6RkdYH1bspBMmyScqjNut16KOBsIi0k7ySqtLutaROu9V1lrs%2FjJ3Me%2BkIfvhwDRbEb75Ix5tZi66cW2Xa4a0lEFZM2Qd3LjDd20rDDS7BgH2keOVK9tnuJ6z878yQ8y60tp%2B8jvzQ1EvJXDOWl&X-Amz-Signature=8582d106bc86787512d9f23e9e3e206a78f9511b883a4b40b6be3518cd98974e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



