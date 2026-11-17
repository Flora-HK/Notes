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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZQIWPJA%2F20261117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261117T101608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQC9SJwwSHHQv%2F0L16JKw%2B5MI2Uq3TUL030bro0Hax7G4wIgdEJEHWgODfyxR7YT0BafeTert1k2k%2Fe%2BloaOm4PDlOEqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL3ARN625o2x%2BishGSrcAzsKLdpGynB%2BYv0mrcwOY3NtldUKwYk0tGSQt9hZhGpGPuqM0xNigVFMNGu8TSWEhCuvi9LNtN5FivoSB842RQstaC11IRCdqDayzoRmua7XRGo%2BtJGLppJ9Gc0%2BRphxiEJPidMEY9sZPHzxQO43bx2JdQrKEsVXv6GRZ96%2FDrvKL%2F6mh%2FvIYqgCHyaQO8BvQdCxw8wo0oZkAJLVfdkpIh6oVPobqSH0Du%2BOfdQxgpZp4qXVeg5BUitDr6LCNq0%2FDlz%2BCst3JesHFHHRRt403TKp541JCpdViMQ13zvr3Vv9X%2BYjh%2FDOJQos6mcXdR4yBS4wSDz%2Fw1xQZfem40zrkJzXJ4hHO5nhomo8gCsid3Ki1iaC3%2FG4%2BOTd82p7M05YdIBEhiJxa0UrXlokg%2FMNEe9tUaraxhMihZyq4q3xRpKb%2F5DKYeBzpm%2B8%2BloqRoMHxBcO%2FkqMlrNLXefEr0G4IoF42yxXfpY%2B%2FkEEMjQelQbHRJnETd%2FOfEmVXkYQF8kK%2FiajcNm%2FmVqk3GV2ak0qDG9m9IO42OEMXllWRbYFolZ2BlRFVQvP5DbdilxdH7U8kTZp4MBwF32B0SZ6fhAD6hhPvO2wiNFe%2BBgBqIoYbEylemUGwYwVlvKtBm%2BDMLmQ8NcGOqUBDMCT6SZbNZDEyvQyTGi14uMbpdJkArmcznbZ39sMTqp%2Bl%2FYbUWXM3FfE8fuG8zGESA0zpalk68PGWkzLTLAiSZ10IqnUx%2Buopxwaf%2FfkUIxHOJmAPsLHuNknNDmgypPUlbU%2FC2CjCQrCSBopAWgdwFVjvx3MHKKkpH63G51fg5QloQFcOdRBCCOkHiIMQpGzWNtpiPgFTK7ifU7bmbw7eMEkIMK8&X-Amz-Signature=82cbc44c44a9440ee9f5e69a8cf5bb1d87dbab3bb81325533c300f0e2d28799f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZQIWPJA%2F20261117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261117T101608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQC9SJwwSHHQv%2F0L16JKw%2B5MI2Uq3TUL030bro0Hax7G4wIgdEJEHWgODfyxR7YT0BafeTert1k2k%2Fe%2BloaOm4PDlOEqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL3ARN625o2x%2BishGSrcAzsKLdpGynB%2BYv0mrcwOY3NtldUKwYk0tGSQt9hZhGpGPuqM0xNigVFMNGu8TSWEhCuvi9LNtN5FivoSB842RQstaC11IRCdqDayzoRmua7XRGo%2BtJGLppJ9Gc0%2BRphxiEJPidMEY9sZPHzxQO43bx2JdQrKEsVXv6GRZ96%2FDrvKL%2F6mh%2FvIYqgCHyaQO8BvQdCxw8wo0oZkAJLVfdkpIh6oVPobqSH0Du%2BOfdQxgpZp4qXVeg5BUitDr6LCNq0%2FDlz%2BCst3JesHFHHRRt403TKp541JCpdViMQ13zvr3Vv9X%2BYjh%2FDOJQos6mcXdR4yBS4wSDz%2Fw1xQZfem40zrkJzXJ4hHO5nhomo8gCsid3Ki1iaC3%2FG4%2BOTd82p7M05YdIBEhiJxa0UrXlokg%2FMNEe9tUaraxhMihZyq4q3xRpKb%2F5DKYeBzpm%2B8%2BloqRoMHxBcO%2FkqMlrNLXefEr0G4IoF42yxXfpY%2B%2FkEEMjQelQbHRJnETd%2FOfEmVXkYQF8kK%2FiajcNm%2FmVqk3GV2ak0qDG9m9IO42OEMXllWRbYFolZ2BlRFVQvP5DbdilxdH7U8kTZp4MBwF32B0SZ6fhAD6hhPvO2wiNFe%2BBgBqIoYbEylemUGwYwVlvKtBm%2BDMLmQ8NcGOqUBDMCT6SZbNZDEyvQyTGi14uMbpdJkArmcznbZ39sMTqp%2Bl%2FYbUWXM3FfE8fuG8zGESA0zpalk68PGWkzLTLAiSZ10IqnUx%2Buopxwaf%2FfkUIxHOJmAPsLHuNknNDmgypPUlbU%2FC2CjCQrCSBopAWgdwFVjvx3MHKKkpH63G51fg5QloQFcOdRBCCOkHiIMQpGzWNtpiPgFTK7ifU7bmbw7eMEkIMK8&X-Amz-Signature=bed355383c03698c15fadf56871047014a2bbdcfdd00c896af175fba326bf959&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



