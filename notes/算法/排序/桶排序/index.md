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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBF45ZW5%2F20261017%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261017T063745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJGMEQCIHv415ajlQVi9YsUTs6hWlEkF7btPD9nQUMU5IjWIiG1AiBT3E6c%2FVnAIJj1oRvXpFGZLRH%2B8B0qqN3v95RCcrmT4SqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjp27x%2FGK5z6vvcQQKtwDiaiWUeO8gPHucc4413Ouf2EwmbbdjkDKFfGkXrEuKsYgEPV9a9N9M0jkr7Z%2FszeBOsMZ7Sbmt%2BInXXrTgE6Af7VIKsmwiuwbQVu%2BMcZ5O0M1feUyIFVAg9c63YlS47CK5FNRJFk3eOBBZmge8g1jR6x%2BsOd29FNPWXPNebBPIqh9txMRSz6F7MtaPUVS5NdAkbGOyfi30jJxlMMTIw%2Bm4nx9KEI5ihmFrhwfwGLpCekwebEs1a0QEQr7nTdOv2GjlVy5ASdPu50qhRl0u%2FAVYn53iEDpSUFQ%2FNp0s3vZ0lHCdNF4MzyZt2nbFu69oazgnqzl22iW%2Fjff18e2Jxxm5YA0IXpEnntYfn03UKvghETtagWiLuq2WALlTe567K7JbZ9d4Q0pF526B5K0Ly%2FZVZ6oQyOq95md%2BF3Ijtenb%2Fp7i8Y9ik4NBWrSSVnx3YTiKgPAxe%2B9jI2Rjwow5ZobyZQjanBcVZ3DSRTFoOLO%2FPTz%2FASggXZhQcRL%2F98WPgQY75GqIWqkUzctwFHktTy7NlxOlE633ESeNaMXVa2xhZD%2BoApKnMcXW%2B0EDAxz4vWJ23ATfIaq31uO2F4g4SlA0z9hxE%2BOY4pLf7dqoDyqk%2FPtT4YMW1YgZVhtD48wjobM1gY6pgFbHFngWuxZuoih5C6UpNuFgmn4WVmjzYSd0RVbnS9LrLmw6commMXgrD58XnZaB8%2F7sg6w7q061RwZ1q%2FH%2FU%2FrJUaJGv14MNhu2EfE%2BT%2BVY4pC8Eo99asBuiAWDQCkhZOVjI%2BFYoCEk0kqw4PzHb5Q4Bw14%2BgGWP3dmZqsm2VsIS6virAd0zONfsfMMI0ydJh%2Bmw6O8Bp1AN4lQaUCkvlk5BABHsu8&X-Amz-Signature=a0ae7528f2d4c0d0fcee5b71d68048e9c91cf05db1b8b689ee3d00e3bd005e12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBF45ZW5%2F20261017%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261017T063745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJGMEQCIHv415ajlQVi9YsUTs6hWlEkF7btPD9nQUMU5IjWIiG1AiBT3E6c%2FVnAIJj1oRvXpFGZLRH%2B8B0qqN3v95RCcrmT4SqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjp27x%2FGK5z6vvcQQKtwDiaiWUeO8gPHucc4413Ouf2EwmbbdjkDKFfGkXrEuKsYgEPV9a9N9M0jkr7Z%2FszeBOsMZ7Sbmt%2BInXXrTgE6Af7VIKsmwiuwbQVu%2BMcZ5O0M1feUyIFVAg9c63YlS47CK5FNRJFk3eOBBZmge8g1jR6x%2BsOd29FNPWXPNebBPIqh9txMRSz6F7MtaPUVS5NdAkbGOyfi30jJxlMMTIw%2Bm4nx9KEI5ihmFrhwfwGLpCekwebEs1a0QEQr7nTdOv2GjlVy5ASdPu50qhRl0u%2FAVYn53iEDpSUFQ%2FNp0s3vZ0lHCdNF4MzyZt2nbFu69oazgnqzl22iW%2Fjff18e2Jxxm5YA0IXpEnntYfn03UKvghETtagWiLuq2WALlTe567K7JbZ9d4Q0pF526B5K0Ly%2FZVZ6oQyOq95md%2BF3Ijtenb%2Fp7i8Y9ik4NBWrSSVnx3YTiKgPAxe%2B9jI2Rjwow5ZobyZQjanBcVZ3DSRTFoOLO%2FPTz%2FASggXZhQcRL%2F98WPgQY75GqIWqkUzctwFHktTy7NlxOlE633ESeNaMXVa2xhZD%2BoApKnMcXW%2B0EDAxz4vWJ23ATfIaq31uO2F4g4SlA0z9hxE%2BOY4pLf7dqoDyqk%2FPtT4YMW1YgZVhtD48wjobM1gY6pgFbHFngWuxZuoih5C6UpNuFgmn4WVmjzYSd0RVbnS9LrLmw6commMXgrD58XnZaB8%2F7sg6w7q061RwZ1q%2FH%2FU%2FrJUaJGv14MNhu2EfE%2BT%2BVY4pC8Eo99asBuiAWDQCkhZOVjI%2BFYoCEk0kqw4PzHb5Q4Bw14%2BgGWP3dmZqsm2VsIS6virAd0zONfsfMMI0ydJh%2Bmw6O8Bp1AN4lQaUCkvlk5BABHsu8&X-Amz-Signature=bdad395e45649ed78ccb720df6bd04afbdf3804d4a6a5bb50ab8f63657bcbb56&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



