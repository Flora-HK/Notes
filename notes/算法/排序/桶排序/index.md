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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTKAF7F5%2F20261014%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261014T070940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpXFYLMPkzoShR1mbfPWA7UlRD8BNddk1q%2Fyij%2BGxUFwIhAKLeJI0gAieHsK%2BXvyuWP5UXVxyEu1GaQQZlywRw0%2FAAKogECLD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzNJ%2FVFbI%2FrKxrihE0q3APud6oT1ESqKl64w1A7OADdBFNbMeydtUgaCH37SsrYIkFRrS2quAC68Us5SJCTZVP8rqPuP3zO5eIsv9DMrsV7boixrfpYcokLw%2B4TMewq1TK0YBiRxOpcr2Ig70XwkaFkg%2FdwrV8KmV%2Bzt7sNpF6KKnjp51q8FLx7y%2Bjdixsq3KfUeWuwSUBMuXrL95F5EDDG5B5zZgsp5Q0yc5yWYZIWanm96194mLYzmOB0%2BmbTkhOZvK%2BdIHj2BlNocuXvjsNxlG5NAX8cRTidhnGzJy1hUBjZSPor0fRy1MuHy4V2M55u0RD8Pifozx%2F%2FBOHfkeldJYWNKXrNUXdifdKu53YWPhDKxU0ju4HyAcRlA8dguYR5S7W%2B4xttC4iy7gT1eB0X892ITbgf2xKc%2BlsNO4Mc2HoWVkoFeTMk5ldxa9ukYPYN2JHTzfKpG8hpldd6ts9ADDr1Vm7yjpfUkiKZquaUpOryCx%2Bm6tUoLKV%2BNe1KGEfjTx6z43X2VIAgAjenxlFxzvH86xTqT8rFfWmD0sb5b%2FteV%2FO%2F1vAyhiJUrWkmvJlXLJ5IkGYZei3AL%2BnBpVjYRC3PuHy%2FImO4MhZ8jBT%2Bv9P99euuzNfvNlOsKEPcMOd84zpkJvXcMU42tzDJ0LzWBjqkAelVQ%2FZb6iuBRj4OjN89mWYyClCabJbj%2B4IbOoR4A3ms6b0yqk6g9H%2FsV%2B%2Bk1gjkCGaEtNEEfSDCabWNGJea2ajuZBp%2F3QIkFPzQsfkpSaWBVMsRFC%2FXW9iuH6DR5b97YMjmMt9HR1%2F53uIn7IURsVRG7%2B%2FudHQz8oCdRpKwdGoLx0Cu20krte6Zjn6lRXdd39rihM7EVKIZG70Re7sJmDrZpeQb&X-Amz-Signature=9a1a9cc1e4307c8db3aaf5a9233f414c66c815f09669dc7ce9d4a7fe1ce098a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTKAF7F5%2F20261014%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261014T070940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpXFYLMPkzoShR1mbfPWA7UlRD8BNddk1q%2Fyij%2BGxUFwIhAKLeJI0gAieHsK%2BXvyuWP5UXVxyEu1GaQQZlywRw0%2FAAKogECLD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzNJ%2FVFbI%2FrKxrihE0q3APud6oT1ESqKl64w1A7OADdBFNbMeydtUgaCH37SsrYIkFRrS2quAC68Us5SJCTZVP8rqPuP3zO5eIsv9DMrsV7boixrfpYcokLw%2B4TMewq1TK0YBiRxOpcr2Ig70XwkaFkg%2FdwrV8KmV%2Bzt7sNpF6KKnjp51q8FLx7y%2Bjdixsq3KfUeWuwSUBMuXrL95F5EDDG5B5zZgsp5Q0yc5yWYZIWanm96194mLYzmOB0%2BmbTkhOZvK%2BdIHj2BlNocuXvjsNxlG5NAX8cRTidhnGzJy1hUBjZSPor0fRy1MuHy4V2M55u0RD8Pifozx%2F%2FBOHfkeldJYWNKXrNUXdifdKu53YWPhDKxU0ju4HyAcRlA8dguYR5S7W%2B4xttC4iy7gT1eB0X892ITbgf2xKc%2BlsNO4Mc2HoWVkoFeTMk5ldxa9ukYPYN2JHTzfKpG8hpldd6ts9ADDr1Vm7yjpfUkiKZquaUpOryCx%2Bm6tUoLKV%2BNe1KGEfjTx6z43X2VIAgAjenxlFxzvH86xTqT8rFfWmD0sb5b%2FteV%2FO%2F1vAyhiJUrWkmvJlXLJ5IkGYZei3AL%2BnBpVjYRC3PuHy%2FImO4MhZ8jBT%2Bv9P99euuzNfvNlOsKEPcMOd84zpkJvXcMU42tzDJ0LzWBjqkAelVQ%2FZb6iuBRj4OjN89mWYyClCabJbj%2B4IbOoR4A3ms6b0yqk6g9H%2FsV%2B%2Bk1gjkCGaEtNEEfSDCabWNGJea2ajuZBp%2F3QIkFPzQsfkpSaWBVMsRFC%2FXW9iuH6DR5b97YMjmMt9HR1%2F53uIn7IURsVRG7%2B%2FudHQz8oCdRpKwdGoLx0Cu20krte6Zjn6lRXdd39rihM7EVKIZG70Re7sJmDrZpeQb&X-Amz-Signature=6417b4d7a8e72bbd2bdef210e000956bc5f1b4567e89e7366adee618863135fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



