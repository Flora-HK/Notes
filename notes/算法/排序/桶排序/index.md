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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y43DOI34%2F20260928%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260928T081741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQC%2BmbJsO2FEyX1e4dhv2FQYPc8NLMq6YxDtZnn%2Fa5%2BpZAIhAPVYZT7pEwq5IoDDmDhekSJzLdx3fndwr8Nyn7Vk3QEPKv8DCC4QABoMNjM3NDIzMTgzODA1Igy1TziqmspACEDWcTwq3AMDQLd96RzQ2CgDjJ4ZqlFQLICFsvRYRskD0EuY95oM6RCzDE6Jin8X%2B1QJwvA01ysG8%2BtQ3fJj6GYtWYmdyvfmryO8T9kPmuLeFmxt2nG%2F3qM91lwjgtLGYTokYMl966xNH1SnYGaaT9C%2F77KrvOLjdt1f4VfnG0m4LID3oq5m0%2F%2Fy0bWX7rtu%2Btn8abytkxAi%2BiNYmuknuYkbWLUtdcXQKm7podS7Hgy1dtqC7LzeuBqQ6qQU4QDwuucBReRT3h3VHrQINAU04ZGm10wtGjUhIlRae5YN9UUETCuX0bOwQngKC9KSK6DnxS8Dc78Xe9EZmv7nvY%2Beo%2Fb0xlaF57cNmngF8gzAGHAVave0w1kyKI5cfUIZYF8eIRS2MbiyvbgftPfYQL%2FNk%2FKsKwK6Oqx7lwhbv%2FdeZpoUB%2F7PxZJM6Y0Mma3dKvfsmsoJRoXUqc%2Bxf1azErUJgdo3HNj9UEpe%2F6ktftBxRXWDUNzlry6gAQUFKXWqfEWOArxhDvMUC2k9Ro8oDbrrEOw%2B9jCypVRZBLMji%2BsCtSeL97DdKcZAUsxTzd5mwMNwEk0hDe75%2B6sD4nUHxqYJr%2B05owFcEU8tWPujyrIuXmuwbuomer58RLym1p4S4TDkO6lFBDCJ8efVBjqkAYzTA3yNivv4ia19jM9enEr%2B0k4lTD3It%2BkN4liXhinRwm6%2BzB761aHmsLpFJCRlnGDvDj1ZX%2B2%2FUM8cLJ%2B%2BAj0p9ds1i8fjRbsAoy%2B8wedM%2B4Ws4wn5ln9%2FL73X5CwRskoWnhM7yf%2BP6V8qW%2FlbhLBDQZsloy8jIqbqa9OnQ8SsQTVY0818K%2BnN4Y7faCjAKlBy2CA%2Bdqt5hEMbHVXpf1JBS1Te&X-Amz-Signature=ee97b0a1a4d50b6fc19045d5773b1b48db4004f7b25d8821d28cb047ee15ec24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y43DOI34%2F20260928%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260928T081741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQC%2BmbJsO2FEyX1e4dhv2FQYPc8NLMq6YxDtZnn%2Fa5%2BpZAIhAPVYZT7pEwq5IoDDmDhekSJzLdx3fndwr8Nyn7Vk3QEPKv8DCC4QABoMNjM3NDIzMTgzODA1Igy1TziqmspACEDWcTwq3AMDQLd96RzQ2CgDjJ4ZqlFQLICFsvRYRskD0EuY95oM6RCzDE6Jin8X%2B1QJwvA01ysG8%2BtQ3fJj6GYtWYmdyvfmryO8T9kPmuLeFmxt2nG%2F3qM91lwjgtLGYTokYMl966xNH1SnYGaaT9C%2F77KrvOLjdt1f4VfnG0m4LID3oq5m0%2F%2Fy0bWX7rtu%2Btn8abytkxAi%2BiNYmuknuYkbWLUtdcXQKm7podS7Hgy1dtqC7LzeuBqQ6qQU4QDwuucBReRT3h3VHrQINAU04ZGm10wtGjUhIlRae5YN9UUETCuX0bOwQngKC9KSK6DnxS8Dc78Xe9EZmv7nvY%2Beo%2Fb0xlaF57cNmngF8gzAGHAVave0w1kyKI5cfUIZYF8eIRS2MbiyvbgftPfYQL%2FNk%2FKsKwK6Oqx7lwhbv%2FdeZpoUB%2F7PxZJM6Y0Mma3dKvfsmsoJRoXUqc%2Bxf1azErUJgdo3HNj9UEpe%2F6ktftBxRXWDUNzlry6gAQUFKXWqfEWOArxhDvMUC2k9Ro8oDbrrEOw%2B9jCypVRZBLMji%2BsCtSeL97DdKcZAUsxTzd5mwMNwEk0hDe75%2B6sD4nUHxqYJr%2B05owFcEU8tWPujyrIuXmuwbuomer58RLym1p4S4TDkO6lFBDCJ8efVBjqkAYzTA3yNivv4ia19jM9enEr%2B0k4lTD3It%2BkN4liXhinRwm6%2BzB761aHmsLpFJCRlnGDvDj1ZX%2B2%2FUM8cLJ%2B%2BAj0p9ds1i8fjRbsAoy%2B8wedM%2B4Ws4wn5ln9%2FL73X5CwRskoWnhM7yf%2BP6V8qW%2FlbhLBDQZsloy8jIqbqa9OnQ8SsQTVY0818K%2BnN4Y7faCjAKlBy2CA%2Bdqt5hEMbHVXpf1JBS1Te&X-Amz-Signature=786d9e14596123b81db62ea6e3e4ddbf54aa9438bc6e57b99396555c98d4a411&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



