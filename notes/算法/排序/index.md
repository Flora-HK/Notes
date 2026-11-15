# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M3PYNSP%2F20261115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261115T085230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICkJTXQ51aG%2BCrWo0Mmg8ZBCPXZBy1s1DKGp2Oue%2BnAFAiEAjwaot4e0KgtFsCaA9042IygzkZ4G%2BeeMcJCCSNeu2jMqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFzU2B85OP%2FzJZXyDSrcAzwYOYfBnblk30gNtWU251J2YkS9Hxci0ZTVfSu9Vk6bIYnrMFVOw3hr7XhDAu2ZSiDi%2B3%2FHctximShZZ2UTqtIERrp%2FYaL3Ta62wted3kDZp64rndS4e0M4Uj2ie9NNuCsJmyKBbuGq47UKM421DuGQ5A5DVs6qRx1WlpC8aN0sisTH680h8eu8wKlway9beP8n0963IaroLRnsBayA%2Bw9TdeYxCiJeeV3qqZmcao5MIdunoibKXpIpBykofe4Sg%2FJgNS9Pm4sIhC4l%2FVi2drF9ippUATvbYSHg7%2BkAKwJrylNjuksVfIY4OphdvpXPmmhIzl6ZoyKpjnb4IFdPzJugZJS0LS0VmUgfwmLcLlB5SzAfiPyV8q5pY6j6CQ5ElpN0bdKg%2BWmNhZHgEin%2FRNMl7DusZ8HjiNIMcfQv1GYPZv173tkvXC6h7Nl6nJjTyzcfKl01zR7STNLByuNQBjpqPyr4TBAuwNHwk55sqpW0H7HpHa%2BV49ciz%2BZEmtyqPDPT7DtndjhgqxosO1AMzrkw%2FSbs%2BrpjN2ndUfbXMGrxn%2BZRXJ9zCuflbZdeeWOkVvn%2BCrdy%2FSXa8rwC%2FcEcYevTsTbAtPZ35cVa%2Bjrm%2FU83p%2FyUxUNKttwvaXfMMJ6d5dcGOqUB0YVQWWkCBkarH7ZjkkfyEGHHt3WyXqYtmAnp81K2%2BTRgXuJXWVrbMCT4WJvSJgxP2q6RRRKIl7u2u%2BheK7ukNJPDs6XV5mgVHEqwFpWZahj1m%2FbEPqioS1cHiXibLzDKDi0D4tjws46XONc7eP72RJSQgh1M6b3K41wEKclHp79%2Fo4e7expPuxR2b0bY7g4DE19HKxmPI0ss7u19C8zV2%2FlqwzH3&X-Amz-Signature=bcbb8ab71d35f4711ce8e9da11bc4c8ac6eef229ad4a267f7764719803c8cfe2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







