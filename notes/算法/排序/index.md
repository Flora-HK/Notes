# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YMLZMPQ%2F20261024%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261024T065448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDD%2FL2XOAbf5ZbQN2%2BWBIadSdBhmG5tUVeKCg0xjA21JAIgbz%2Fji1%2FJqCSqVv3Q2QEK9j3lLzSDRL8frqGN82CDQd0qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBwuxVc4Oy8Nuq51CCrcAxNpnaO0H7h8%2B2PEEE1H2K9g%2FURVKqjFSNMkw1%2FeuDER3s3eo7J8urtzUs%2FmMJ34FTGH%2B1ZikRY6vg5Uraaj6vpRSSVb%2Fyx57GmHKJzy4n26fdfjFRAg999AD08oZU9r9kx6DUvn12nrk6UNayrUQxOmOC0xWDqOHjAyGIwr3G9In5GeZLsUzL%2BYlroqRH068kVCSIrYYmuiE4r2VUkWvqZazxh3XzOIbgkI3LzA5XwwPY1BlozcssDXhDiePatpuux44i%2BKPTY5sKnEltknY10O7UmaOXK8DgX6LQawXE71E2VAxfLq6ytKrgIm4usTBMq5B9TtIUBDmYc5wvTOEG4sFV8zHlJEHFsyGjl5RvVlp%2FgtADxszb1rkkCMVAm9LVRY8qLOInKS3Sn%2BT%2FML1I1QqzfNWs39lCSlw4baKlfpsKDgx80HKL7AvB47k%2FKp7WLE%2BVmPSEx6G43RisuaYHdukeJDmbJ1otQAVY0tydE7roBdouysSIuR5e%2BSDoY8nbmAH0BOq3lMRoB2Ado7FQ9yF%2B%2BI%2BQfDqzqz0rUUjpYQ0vzsW9wos882UMOklNQCPMxWxHm1LFV%2FGIREh0QM%2F%2FopyKaQpiU28EnMAPwu1vK6BvraCm0rlLdEnF9EMJWE8dYGOqUBFsKWYFy1Ib7RXNOxIGYPysNwH8nmxWWzwWaYjL5oln3Gwnh18sRo5kVs1iLrIG8vP7yTdwbeDLjJ3%2BDbr7jxSsh%2BHuTj8fFI0tEJtwIcEuWDu%2FNpe53bDQaXy7AroymrPWtw169LFjV9UMZVsOyydwkJO9fuHCZIMzmA6jivz4QWNBY72KBx75YZPjpTsbHfuGVoYkJtulX1GQ%2BEr1Q5smi%2B32%2Bb&X-Amz-Signature=63808d2813599f85260c7a402faa8557c486a69a5f969008ff2b38836d3cf74d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







