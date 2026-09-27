# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LEAFQNY%2F20260927%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260927T073927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQCQli0lmbT70qGTkgwmYGuHT1N6Tvfu4CasQtBU5Jpc6wIhAPYE8%2FngTbidicpdfYS0IvqZcZnhfMHdreHD%2B6abEeEIKv8DCBgQABoMNjM3NDIzMTgzODA1IgwWzZhDaOWBQ%2BjrInoq3AOucCin2DuLIMiXz0mnAY5aFFKZxsqIHELlVgquma7u1YhTucR%2BoH3w0pByoAjXlG3b3mygz66HsoCofiEKNYLmE6QRbth6Fq0qi0cGV5XO915Syj5mLDKDtvFgO2Ei53QaXcArr2t6%2FFBR5twe1J82%2BMzSUo7HzhXnpLTBXJzVis%2BNj28cMC5X9j6TpQ7pKjgZP4KRuRjMzO%2BxJg7Y2OLeUtfVKh5iRHqX7UJFxHJNdsSh3reZSQcenccGmsJcjUn8b06o7qJsGv5Ngrrq8Rf88P3qF%2BduXeo2pElXPMfu03Om0j%2F086DoUFSaUJtt15RCnOnFIWHYqRkse39foVxucDkICtfuN9AYC8xF1C8guC%2Bdl6QBARUyQVjiYHGIcBymieDhUhIa%2BTcJQjKWvYVR6qZa6SX2NJRmdLyqsl1m5EJgXE2zPz7icBH0AafONqRLwSkPGJBA2k8OzzvMMbPuVGgZFEXNzxQvuTJjaaGlyUivjavUfW6VFc2OUPqK9%2FYsYxsgswOhwvC30cYoXSkBMclnNaiNDiT2ZwoM5BdaMhvgNNrS7VDMiokLzYqmFHbIQ9tRLUpkzoomUiLFejC9AAwjhhr%2B%2FXSgKgphyUdYvR%2BczYtxKqWT1N6jwTCN9OLVBjqkAcSgveQN8SIJXmzAwrvriB%2Bb3IOK8VbdJsWV4CSfmXC%2BcdF2yuxmG3RUMenL3GC4Xu2DDuDp0IGHQrpxD7EQ2NjjmW%2B79%2FxXjssaySa%2Fqe4CjnXcHOvBNAg5dyfnVRp3KqyD1SYZqMal4ws4Z%2BhUGdKfw72Mw91ooD%2FAP4HDMYaFXhtK2h5qguMogX2ggHZytuYNaWP5KhJdYpkl87Zx%2Bv26C8wM&X-Amz-Signature=eef48256a68712255bfe1837a2113859b381cf6961d04610baf133f9be7d0773&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

说明：

- `n`：元素个数。
- `k`：计数排序中的数值范围，或桶排序中的桶数量。
- `d`：基数排序中的位数。
- 稳定性：排序后相同关键字的元素相对顺序是否保持不变。稳定：保持；不稳定：可能改变。
- 快速排序的空间复杂度主要是递归调用栈，平均 O(log n)，最坏 O(n)。
- 希尔排序的时间复杂度与增量序列选择有关，因此不同实现会有差异。
- 计数排序、桶排序、基数排序属于非比较排序，通常对数据范围或数据类型有要求。

综合排序：在选择某种算法的时候，除了直接考虑时间复杂度和空间复杂度之外，还可以根据**数据量情况**来分层进行排序，在样本量较少的时候使用插入排序较快，在其他情况情况下使用其他排序；也可以根据**稳定性**进行区分：基础性数据使用快速排序，非基础性数据使用归并排序。

两大不可能：基于比较的排序不可能时间复杂度小于 `O(N*logN)` ；时间复杂度 `O(N*logN)` ，空间复杂度小于 `O(N)` ，具有稳定性的排序算法不存在

一、基于比较的排序：

二、不基于比较的排序：

三、算法稳定性：

1. 定义：对于一个待排数组arr，如果使用算法A对其进行排序之后，其中相等的元素的相对次序还能保证跟排序前一样，那么这种算法A就是稳定的。（对于基础类型数组没有应用价值，对非基础类型数组有应用价值）例如如下情景：
1. 符合算法稳定性的算法（直接进行较远位置的交换一般都不稳定）： 







