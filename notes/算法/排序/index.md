# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJO2UM3Z%2F20260925%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260925T071105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIF8DlnbiBW%2FL3pW2d4fT2L6Q0Q6ocINnArRCe8JjEK4TAiB1lw%2FtdXXfyFs23JZZBAOe49DPpOudDGJWmTFK2KF8fCqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMekJnendTdSlPzxfSKtwDbr74r9OWoNY4a7NK9eqXM1DzVqDCJFM%2FpXy2ofv%2BYyuhzMTtnMdRx75oBFY%2FzLslUyfDvNvOaqKwzIegD6i8EDm53YRLyNIrDdRmPLNv28ARR99Dktb5wbEVJyNhKK6S0z6yDd3FQomTtUuPSVRhDAAK0vEWayMD7dqHA2hWHr5Vhmq10S0jq0WMZCUyL%2BOos6amrswAgNzHfbemuXAae7UvoU49FQ1LIDnRHAgn5nmFHbmt8ksQTiS2C3wUvi14VUto4dUh9bIQ2%2FVCPnxnmPMTQODxdi4409DLVTd2lM%2BfXtEid0LQRfKQ5T2MeYDuENzpQWCPqnuyJ%2FibpQ3o7vE8h3aW4C6NOy2cP32tNUv%2FLOvHe%2BPF49Gff%2Bdpkd1VpBGQKlUZ60HoUUPVGtQ3k5MXs8aNmwTJ7dM3THx8qsAbXC9Etih7Aov5cvpF5KRPPmIvp%2FhpHIaIqat4nIr9eQfTeokFUt2bSLj%2BIvhkWK4FxzSeZfbwkSJIlUMlCQ1Tk2tTwJ5rp2WcGyc9FCDj3KJ3cZKA%2BDKJqYJEqkNSURM%2B8RW0YMVOOJK7vlTlNRsqY9gpwxPLdQQtEKcXb7e1HHmMCQ%2FMdm9Vb7nchbEEQwLdXnTMQUjADybZaSAwzZ7Y1QY6pgE5gkSpt%2Fn3BvrcMrs8yZMHM0o41z0K9cKmMuWIni8aJGSrqVv7ffJWHvwdqKHWYv8rBJ0lXX%2Bazs%2FmJcjCggkqTPfDqsrS7TuP%2FH%2Fo9YSazhGBn1j9OsZ%2ByGYWAORj%2FzlHtgN3NUiC5QX%2BsTRLrEQW3BP8rNsfUneF0oky%2FRBtfoa4n5tx88HyOvwIVErFhXoKvC%2FLDrZg9Hgx4e3Qhz0PlbbWHlAt&X-Amz-Signature=bedc7603515f644d6182c74ca3098aa9090e07f33cb711b80b4d657a15155c1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







