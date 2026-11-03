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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5II6QYS%2F20261103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261103T090416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVWI0KJFNIzItXmA5ZU%2BpvgUPIjFoZOazILFBk7qAAygIgWFz2UyLwC3KPrtpBQmJ5UMpIQ8W%2FBYqVHClLc6zex6UqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK5CIEU5mpVvjotoqSrcA7%2FdZL9h0yRVvE7DSpFlResOsOJC7Z8xmw6RlAC6nBJqJQ94nlou%2BGdJb0PcrVKO4GYZcCfDpDNZ1PwkkGnj6%2FKVm3uIBkOtrlQ3QBSwurgOYYUOw0eFSTrNNwnnEa81tWXC3p%2BCI81h5x7i9vGbI4vusbJADgvbD2n6HPm2IRs8GobjsU03JtgnlSRQOwXHEDf0PAKYbC14DFDbiGuP8fFRJFzSHl4Y%2B904tIG4p2ba78yIA8LXDK%2BraLNw%2FvSNvE74fqrFrM9NVeTH2qeRAfZidHYV0UhGtrWxDdl6R37oPAswaPox16LcQapN0JCGOOeUoysLC5yB4bXFqUKFH%2FAlP1oqqlSWPGs1g4IUW%2FjYQDLNWZ%2BwU2VMZVaX%2Ftmy9zBp9U74fklMqCYuRsLhjW3qWEmQk0dCF6doA%2F%2B2ETIKV9IH%2FmiWXdF8xFxoEeLCZVcP1DPEUU2AWpQhEWK9yDINn4H1gbJCLNHMoQmV4qzaIni00ENrq%2BwAvvFrao9X0Wq06BBZMYwqL38d%2FivbRQZA4EQIHPNM%2Bi2TU4hCMG7Gx14wf1QQowcY8imraOspZ0Z0SOY5IClm%2FpCtzSDvyHA5GoaVsWFAqjjGrsRLQnyHgygHyaM59ZQVk0WcMLGKptcGOqUBTlwZU9PzuixHFGsMkeqee8PN%2BtUxYBAsS02dUvy7G3UJW6fcD7bF1OTCySz8Z91AaNlNY52W%2BQhRp5V5Q4NkA4b%2FHESGo4hTlPWoJxB%2BSYUlUq9tDJEnJOZ24Ak1RH4c2jBD65L4lNIWFSufRy58fnicTwaTTJWbuYQMNBlDDhlhB4nA5djUs96%2BcqU8ug8Brkcir5F1QIb7vi5ILdqDnH3EBOnD&X-Amz-Signature=f563df8fcdd03d751ce31d0aaa79cef432d6ab3b2f148b22475c2985e78ac55c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5II6QYS%2F20261103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261103T090416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVWI0KJFNIzItXmA5ZU%2BpvgUPIjFoZOazILFBk7qAAygIgWFz2UyLwC3KPrtpBQmJ5UMpIQ8W%2FBYqVHClLc6zex6UqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK5CIEU5mpVvjotoqSrcA7%2FdZL9h0yRVvE7DSpFlResOsOJC7Z8xmw6RlAC6nBJqJQ94nlou%2BGdJb0PcrVKO4GYZcCfDpDNZ1PwkkGnj6%2FKVm3uIBkOtrlQ3QBSwurgOYYUOw0eFSTrNNwnnEa81tWXC3p%2BCI81h5x7i9vGbI4vusbJADgvbD2n6HPm2IRs8GobjsU03JtgnlSRQOwXHEDf0PAKYbC14DFDbiGuP8fFRJFzSHl4Y%2B904tIG4p2ba78yIA8LXDK%2BraLNw%2FvSNvE74fqrFrM9NVeTH2qeRAfZidHYV0UhGtrWxDdl6R37oPAswaPox16LcQapN0JCGOOeUoysLC5yB4bXFqUKFH%2FAlP1oqqlSWPGs1g4IUW%2FjYQDLNWZ%2BwU2VMZVaX%2Ftmy9zBp9U74fklMqCYuRsLhjW3qWEmQk0dCF6doA%2F%2B2ETIKV9IH%2FmiWXdF8xFxoEeLCZVcP1DPEUU2AWpQhEWK9yDINn4H1gbJCLNHMoQmV4qzaIni00ENrq%2BwAvvFrao9X0Wq06BBZMYwqL38d%2FivbRQZA4EQIHPNM%2Bi2TU4hCMG7Gx14wf1QQowcY8imraOspZ0Z0SOY5IClm%2FpCtzSDvyHA5GoaVsWFAqjjGrsRLQnyHgygHyaM59ZQVk0WcMLGKptcGOqUBTlwZU9PzuixHFGsMkeqee8PN%2BtUxYBAsS02dUvy7G3UJW6fcD7bF1OTCySz8Z91AaNlNY52W%2BQhRp5V5Q4NkA4b%2FHESGo4hTlPWoJxB%2BSYUlUq9tDJEnJOZ24Ak1RH4c2jBD65L4lNIWFSufRy58fnicTwaTTJWbuYQMNBlDDhlhB4nA5djUs96%2BcqU8ug8Brkcir5F1QIb7vi5ILdqDnH3EBOnD&X-Amz-Signature=1da2e5429ca011a3f6665a806934e1bf343f71a1bad6cd2c5f72a8974a580da9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



