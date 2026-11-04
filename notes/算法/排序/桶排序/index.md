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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBAVVMVO%2F20261104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261104T084129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJ0OEroU8dAKD0tMtVJ1S0Imc7cllWAJMq4rL2Aa9v6AIgXK75y1gTB94LsryX1mVPEsesI5CHwSNG%2BRbftDVLoJIqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNPsoVvZfR3YWceMtSrcA1PY%2BohMlJj4OIcwrDPlD%2BQjbzHdCaRGstpdkeGpIExtWN1xX25XR9fU%2FG872BAlDeKzJA2R%2FHwGH0DLXiYW2jxY%2BiaTNOfTB7I3XPSY2fDsDr6f9r53IJ0GMLC2wk%2BHLQQAEHGi7cUhPC6JpfHQwE%2FdTXN0Ny%2FPUI%2BMdZad48vYlMpwzTKGn169mvD5DZAwdA8XLYWtrv0tZktHTJARe%2F9t5FeJzlWfYSpYozXc9LfWU9CQWiTiiccfRoYEudBj0yyW4toEsHBhfnh6REInyVSlBxzDt2gkCjGPQRAUSM3Qky%2FW8FEn0TX75hcxYPwNTkUqDdr9%2FP8%2Fo5jAKFmyHibEGkDAHzdjZQ74nkSuh9l3XtCTDVBuONcSFZZA%2Fc0TfSab%2F9x39w7Sl2g35yqT2qLqqRSiFoRdpRwht1zHDLlXy9YrwD5yqqrHdb6MhJhcvLN7eGuD6xdzZQifdM6p%2FN%2BvL3hxmawIxrnkOtDMCxC%2B3MGw5tGixVlmeVs7JsZ7sqCLLRKFVWZ4fUQDIGMM%2BjNQ5rG05472WnYuJ99fDCF3Zu8SpR%2FB8xgnGs27AKdPaJJbI3sVNTAAAUR3vbU8FEkmWdQR85u0gvF9GXamIubWzG2%2FkSpX1%2Fhl%2BXEXMISNq9cGOqUB7FqZ96%2BfQsABAN35vqrRecCMxN6bQhGgMHl9trwlRjmg9LE0ZyBx3t2cvc0aZUbKmPPIkCigC4NPpStyJxRs4ECTslNaM7XvbwnuEROL%2B2wplimdTzGLemJ5CP7FZobF9R3xY%2FB3PNnlpaR%2F9iN6kjoPJYzgG9ui8gB%2FQ4xYX8%2B4Go9NY7HYYcRLFlM8JGDuNpoOA95ymkJ%2BncTZEfDKjLqhGseK&X-Amz-Signature=d315a899a9e6caf530a3cd10bd64f5b233a1094360a22d2ad61535b83a75a161&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBAVVMVO%2F20261104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261104T084129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJ0OEroU8dAKD0tMtVJ1S0Imc7cllWAJMq4rL2Aa9v6AIgXK75y1gTB94LsryX1mVPEsesI5CHwSNG%2BRbftDVLoJIqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNPsoVvZfR3YWceMtSrcA1PY%2BohMlJj4OIcwrDPlD%2BQjbzHdCaRGstpdkeGpIExtWN1xX25XR9fU%2FG872BAlDeKzJA2R%2FHwGH0DLXiYW2jxY%2BiaTNOfTB7I3XPSY2fDsDr6f9r53IJ0GMLC2wk%2BHLQQAEHGi7cUhPC6JpfHQwE%2FdTXN0Ny%2FPUI%2BMdZad48vYlMpwzTKGn169mvD5DZAwdA8XLYWtrv0tZktHTJARe%2F9t5FeJzlWfYSpYozXc9LfWU9CQWiTiiccfRoYEudBj0yyW4toEsHBhfnh6REInyVSlBxzDt2gkCjGPQRAUSM3Qky%2FW8FEn0TX75hcxYPwNTkUqDdr9%2FP8%2Fo5jAKFmyHibEGkDAHzdjZQ74nkSuh9l3XtCTDVBuONcSFZZA%2Fc0TfSab%2F9x39w7Sl2g35yqT2qLqqRSiFoRdpRwht1zHDLlXy9YrwD5yqqrHdb6MhJhcvLN7eGuD6xdzZQifdM6p%2FN%2BvL3hxmawIxrnkOtDMCxC%2B3MGw5tGixVlmeVs7JsZ7sqCLLRKFVWZ4fUQDIGMM%2BjNQ5rG05472WnYuJ99fDCF3Zu8SpR%2FB8xgnGs27AKdPaJJbI3sVNTAAAUR3vbU8FEkmWdQR85u0gvF9GXamIubWzG2%2FkSpX1%2Fhl%2BXEXMISNq9cGOqUB7FqZ96%2BfQsABAN35vqrRecCMxN6bQhGgMHl9trwlRjmg9LE0ZyBx3t2cvc0aZUbKmPPIkCigC4NPpStyJxRs4ECTslNaM7XvbwnuEROL%2B2wplimdTzGLemJ5CP7FZobF9R3xY%2FB3PNnlpaR%2F9iN6kjoPJYzgG9ui8gB%2FQ4xYX8%2B4Go9NY7HYYcRLFlM8JGDuNpoOA95ymkJ%2BncTZEfDKjLqhGseK&X-Amz-Signature=4837e77fc034e26d4fc390cf09bc1781f9e91ff343047a0f6a0e5d64985de1f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



