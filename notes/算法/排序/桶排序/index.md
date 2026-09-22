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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GOCVB5M%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T072303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCX%2FPUSyZZBa7nZfOAFOn%2F5KNK%2B7CY3m%2F8Jw6w29SKxBgIhAJ9Rgf2N%2B4vHYrsio0dOFyW3Lm2gsOE34Kj6JzqBdlIEKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGLk8mp1NFUaKWW2Yq3ANGpCLZJPccZklydEaf0Gx769XYsksww%2Fk7U1sYQTqt5WqrZnxVQc3MOCxq%2FT9kliT%2F0fJuBBl5RKPijUwDgt%2F9bkolmTq6SfpoiNbLfHXwQz6c6O3PMc0J5VKDXQ5DAnNi0PkKlHJv63oWf4lg0bdJFQYSJW%2BNRIc6Ih35waThsuSqBRJQ3b%2FPJFPNiQ%2Buzp9RbKOFWvqSy6Fr1jPV0jn%2Byui1nD4dUmgY1BUENNK%2FUL1dDEna3YZuQNvwivyEj%2F3fzNgKhSZYf5JXCWrAOM3Aav3u44G4zgzfnEqPBTOK1vfhUG0fZFBe77sfT8grNiG00JELDJUCsrhgPiwfdiQNSYqIn1YCp933Y0HIwZCVm8y7MssOS8XUdkXrusGQ1Kt0mGazgcTYCm8qq9c0FLNOs8QU4mCU4bz6MIDLTVGwk2Ho6UrlPrXIx5Lgv5lBYEG7dQ0wxudZx9HksO4R%2Bx1nB2Od1EDeK6HRK1PMBI%2BljdtcgSh3Ql5sBD5z6OkRnI982l3O9wAPrVxPrLHGwmR6enWLCW7wAVqywF0ujAE%2B%2BfyqKbGyKSeUfPO4nb63nuPZHcjNXrIgVO1xu42D8EFd7n1UplMhNU%2BlLcPQGaOJGdf6FQ0XZM69WgcRODD3wcjVBjqkAcFtPvT0jlNiFZi%2FkSMKRmAq1HJO1xq8ifSs2QAHxAE3eu7whQt7%2BJDMRGfdQ19sGKasrK93fjXn04TZqigY6NVoBp5SelMJX7a36%2BIfe7%2FZjSssyjdjTTOHXKz8YtI1QzANwF8ZRumA36hB%2Bb1nmILCV22c9Frhp3n%2BaRdkdT5siy3%2FqU70dKMZtSnd377UkMdRXNYaz4c0W02OQncsi%2F7C219V&X-Amz-Signature=0c679e0ad726a3bd6632b6a47ef6511a8ca131e15c2125c3a03a48e45f5e7828&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GOCVB5M%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T072303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCX%2FPUSyZZBa7nZfOAFOn%2F5KNK%2B7CY3m%2F8Jw6w29SKxBgIhAJ9Rgf2N%2B4vHYrsio0dOFyW3Lm2gsOE34Kj6JzqBdlIEKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGLk8mp1NFUaKWW2Yq3ANGpCLZJPccZklydEaf0Gx769XYsksww%2Fk7U1sYQTqt5WqrZnxVQc3MOCxq%2FT9kliT%2F0fJuBBl5RKPijUwDgt%2F9bkolmTq6SfpoiNbLfHXwQz6c6O3PMc0J5VKDXQ5DAnNi0PkKlHJv63oWf4lg0bdJFQYSJW%2BNRIc6Ih35waThsuSqBRJQ3b%2FPJFPNiQ%2Buzp9RbKOFWvqSy6Fr1jPV0jn%2Byui1nD4dUmgY1BUENNK%2FUL1dDEna3YZuQNvwivyEj%2F3fzNgKhSZYf5JXCWrAOM3Aav3u44G4zgzfnEqPBTOK1vfhUG0fZFBe77sfT8grNiG00JELDJUCsrhgPiwfdiQNSYqIn1YCp933Y0HIwZCVm8y7MssOS8XUdkXrusGQ1Kt0mGazgcTYCm8qq9c0FLNOs8QU4mCU4bz6MIDLTVGwk2Ho6UrlPrXIx5Lgv5lBYEG7dQ0wxudZx9HksO4R%2Bx1nB2Od1EDeK6HRK1PMBI%2BljdtcgSh3Ql5sBD5z6OkRnI982l3O9wAPrVxPrLHGwmR6enWLCW7wAVqywF0ujAE%2B%2BfyqKbGyKSeUfPO4nb63nuPZHcjNXrIgVO1xu42D8EFd7n1UplMhNU%2BlLcPQGaOJGdf6FQ0XZM69WgcRODD3wcjVBjqkAcFtPvT0jlNiFZi%2FkSMKRmAq1HJO1xq8ifSs2QAHxAE3eu7whQt7%2BJDMRGfdQ19sGKasrK93fjXn04TZqigY6NVoBp5SelMJX7a36%2BIfe7%2FZjSssyjdjTTOHXKz8YtI1QzANwF8ZRumA36hB%2Bb1nmILCV22c9Frhp3n%2BaRdkdT5siy3%2FqU70dKMZtSnd377UkMdRXNYaz4c0W02OQncsi%2F7C219V&X-Amz-Signature=6367a42d20c6d5723d6d35e1796687d00b0c8d6079bea7d398f65b220e879751&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



