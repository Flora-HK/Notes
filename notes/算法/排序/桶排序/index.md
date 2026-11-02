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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3RTA2C5%2F20261102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261102T085628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA13O6WXfryezbQoqtoTKqYIH8J16Jv4%2BHxtegMm6Gw%2BAiEA%2FpMNr4KdEuMEoFrKN6xOEiDjSzfJ014IXbYdizkUp2Iq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDAPy2rVt3rOazyRngCrcA1utswC%2ByNVa0UXSlJZbd8iWbzyuNFl1UbvmkVvwZ1mX0IA3XZKgbWB2GFc0FEJjPFO0r5d2JwgxXA%2F%2Flz8nWa8p%2FlZbjo3aGn4TUDzDwD6OnqL2QpiXgt0el14fOVJI39S8ZX0u3eG2gy4FKP6S5ejIb3Wj1mRV2MmRpMCAMfr3qoXByCKlYUswVMr9t4sjmtouvP1eGfikMnFzZv4pL0Owb4zCfNZmc%2Fkme5ATiDJ7QAwdX%2FR019Qohv1H%2FawaiNV7oFa3ZWu7xZA92qsZmupVey9g5nFiCRpgnQACSbkqI9eTfvKmX%2BbTz%2FKIOMUEF87RN%2FJ4QOlgaJW18FJou86oAQsTkbRTbBQ9iOSXCA%2FXmjFdECRmrY0jrzxUTrpSqJOvb0whqsHsQxEr4xJ5j%2Bhj11as2xVy%2BLhKMQnVZtYGRm8Nuk2Qxz8kLeHyEWISGujF1zm5t6qoKK8rCoRrB9goCEDWcISwnHRlQ3Cm4d4A2fbbHFJRhp8jS6Y7gXDFOHPf2dYCT89dA9XTwG41KHpIrBGPBOyYxv7KPKiC91s8FrALiGImfQ0CwentuwZsmyOIN4AcpFO1AQdEmMdKQXbrIGO%2BnCwbr9CluwPcgFmZ5woXjDPhC8SB%2F6B3MJSRodcGOqUBfxOQk%2FjYoxR7XomfsZS%2BDuQU96ZHY%2BO7OTWXTl2NObkVOJZRC%2Fo3%2BvWddiEiAJrTMgFByxOFm%2F9Az3DT69xnpRVjJKUOGOlB2lR3nTK2MprqZRTRaoeghz%2ByUY5GuEw6brDPrzBwA9MQIoDQk8BtyYbeOGKc%2BKo%2FBt2KaSJuNIq7fT56ZtIRRW2O5DP8gxu5L1VeKG6zOFJBp7R0up7LfKfAcEWV&X-Amz-Signature=c066fb37229f8b98799b111e4f9793815aa7e4182f1db8dafb46e7f852e78755&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3RTA2C5%2F20261102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261102T085628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA13O6WXfryezbQoqtoTKqYIH8J16Jv4%2BHxtegMm6Gw%2BAiEA%2FpMNr4KdEuMEoFrKN6xOEiDjSzfJ014IXbYdizkUp2Iq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDAPy2rVt3rOazyRngCrcA1utswC%2ByNVa0UXSlJZbd8iWbzyuNFl1UbvmkVvwZ1mX0IA3XZKgbWB2GFc0FEJjPFO0r5d2JwgxXA%2F%2Flz8nWa8p%2FlZbjo3aGn4TUDzDwD6OnqL2QpiXgt0el14fOVJI39S8ZX0u3eG2gy4FKP6S5ejIb3Wj1mRV2MmRpMCAMfr3qoXByCKlYUswVMr9t4sjmtouvP1eGfikMnFzZv4pL0Owb4zCfNZmc%2Fkme5ATiDJ7QAwdX%2FR019Qohv1H%2FawaiNV7oFa3ZWu7xZA92qsZmupVey9g5nFiCRpgnQACSbkqI9eTfvKmX%2BbTz%2FKIOMUEF87RN%2FJ4QOlgaJW18FJou86oAQsTkbRTbBQ9iOSXCA%2FXmjFdECRmrY0jrzxUTrpSqJOvb0whqsHsQxEr4xJ5j%2Bhj11as2xVy%2BLhKMQnVZtYGRm8Nuk2Qxz8kLeHyEWISGujF1zm5t6qoKK8rCoRrB9goCEDWcISwnHRlQ3Cm4d4A2fbbHFJRhp8jS6Y7gXDFOHPf2dYCT89dA9XTwG41KHpIrBGPBOyYxv7KPKiC91s8FrALiGImfQ0CwentuwZsmyOIN4AcpFO1AQdEmMdKQXbrIGO%2BnCwbr9CluwPcgFmZ5woXjDPhC8SB%2F6B3MJSRodcGOqUBfxOQk%2FjYoxR7XomfsZS%2BDuQU96ZHY%2BO7OTWXTl2NObkVOJZRC%2Fo3%2BvWddiEiAJrTMgFByxOFm%2F9Az3DT69xnpRVjJKUOGOlB2lR3nTK2MprqZRTRaoeghz%2ByUY5GuEw6brDPrzBwA9MQIoDQk8BtyYbeOGKc%2BKo%2FBt2KaSJuNIq7fT56ZtIRRW2O5DP8gxu5L1VeKG6zOFJBp7R0up7LfKfAcEWV&X-Amz-Signature=8338bd3fd3065f6e6ce925bed1b6d9df0be13349891d0c5353ac6456def51c7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



