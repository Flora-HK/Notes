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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665J4RD4XD%2F20261118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261118T094754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCh55bF6aKeiQaNPXML%2FQbG%2Bzw75XYqMVthsLSeinde1gIhAP4m%2BPLRuivy8G1JY4NUp5ZbfAXls3g%2FFUlQT7yR9kH9KogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVI7PI6nWtBiKyk2oq3AOrXDFbd6rPZgPOfZY7S2C%2BdDmkFRemezde7T83sQIeTg5%2F8rfeq2qjj4pXeaAMwTYJToHZYQ5Zw9Kl0syc9lwdvDSMwHIiM7kiLDLqjdMIZ2fmBk6bbnKVRB9SrwvRBsv1whubYsZpym5%2BsAgOQOz2Wzoz%2Bf0qX4%2BdIinPEzoRBkinAOobSSXkFquh5FXGi2crnKGQBlkpZmhSSc%2BOlnVsdFz5aEHRIm%2BG6EkIxhbeygpa1bSA09a2z15Z6eB5a%2BoxjgaumIXLJLa%2BAcwg5423NYNDNyYLZ%2FUQaNtkMZQ8faJtFZfe%2FaNtRIWIJmp15cv%2B9ihbHi5AQB%2FDkf%2FmPnN9zN%2FvipLP5LD%2Bj%2BSw1GWhqtL1hqVGA4x9DctdUR2esVMsOCdzKHlEpSSrkwCvJ0zxjEqdy9fvVJkK0ekvREEBTvEFQhiVPPMHBtfs63alL3iWZb86M4FzsVzBNT7XoEWz48Hb4wlPjN5TwH1UmQSN7eh%2FFu%2BhO1G6XJsD0uPPbjeG8GZWGaiUFIxKlwoXlqT%2Bmr%2Bej2mkmvg%2BZtdNE4uIaSDnlKqBxKZKSyMZCnyYpL%2FehWNR77UPYuNbHtR4Ozc8vRsgjWCyQKb5P3kvYZb3wVVEO5QaF%2B%2FOaKrfMjCT0%2FXXBjqkAXQ3DA8XJBZViZcuRQzZtTmDmkTOD%2BUTGlhTIlZZ7CjakCrYHdjRlfM20IknRyNQpd4Ml6Zitbv3o4%2Bc7loOC1hUBRN%2Btv671SvOZdW%2Fy1nTvrZ3i6F0vHoQLaRuhrCk7wI%2BZjAcsQRGd4jHGCzCPePAjy1VrxbC9Or9G88wppTuzsu%2FdpkmzDFj6PDUawI7EItABXE6kBU4N%2BxHCqdgpI9FA%2F1d&X-Amz-Signature=dcfce17b2bae1f4ca21df1112a031a9729d25bc6ea73afe809728fd12b37396d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665J4RD4XD%2F20261118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261118T094754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCh55bF6aKeiQaNPXML%2FQbG%2Bzw75XYqMVthsLSeinde1gIhAP4m%2BPLRuivy8G1JY4NUp5ZbfAXls3g%2FFUlQT7yR9kH9KogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVI7PI6nWtBiKyk2oq3AOrXDFbd6rPZgPOfZY7S2C%2BdDmkFRemezde7T83sQIeTg5%2F8rfeq2qjj4pXeaAMwTYJToHZYQ5Zw9Kl0syc9lwdvDSMwHIiM7kiLDLqjdMIZ2fmBk6bbnKVRB9SrwvRBsv1whubYsZpym5%2BsAgOQOz2Wzoz%2Bf0qX4%2BdIinPEzoRBkinAOobSSXkFquh5FXGi2crnKGQBlkpZmhSSc%2BOlnVsdFz5aEHRIm%2BG6EkIxhbeygpa1bSA09a2z15Z6eB5a%2BoxjgaumIXLJLa%2BAcwg5423NYNDNyYLZ%2FUQaNtkMZQ8faJtFZfe%2FaNtRIWIJmp15cv%2B9ihbHi5AQB%2FDkf%2FmPnN9zN%2FvipLP5LD%2Bj%2BSw1GWhqtL1hqVGA4x9DctdUR2esVMsOCdzKHlEpSSrkwCvJ0zxjEqdy9fvVJkK0ekvREEBTvEFQhiVPPMHBtfs63alL3iWZb86M4FzsVzBNT7XoEWz48Hb4wlPjN5TwH1UmQSN7eh%2FFu%2BhO1G6XJsD0uPPbjeG8GZWGaiUFIxKlwoXlqT%2Bmr%2Bej2mkmvg%2BZtdNE4uIaSDnlKqBxKZKSyMZCnyYpL%2FehWNR77UPYuNbHtR4Ozc8vRsgjWCyQKb5P3kvYZb3wVVEO5QaF%2B%2FOaKrfMjCT0%2FXXBjqkAXQ3DA8XJBZViZcuRQzZtTmDmkTOD%2BUTGlhTIlZZ7CjakCrYHdjRlfM20IknRyNQpd4Ml6Zitbv3o4%2Bc7loOC1hUBRN%2Btv671SvOZdW%2Fy1nTvrZ3i6F0vHoQLaRuhrCk7wI%2BZjAcsQRGd4jHGCzCPePAjy1VrxbC9Or9G88wppTuzsu%2FdpkmzDFj6PDUawI7EItABXE6kBU4N%2BxHCqdgpI9FA%2F1d&X-Amz-Signature=54b037679b85cb8dd101fbfe126da25c3601e42b69d1daf0433a87ec75f1ea91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



