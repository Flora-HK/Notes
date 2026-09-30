# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VQFH54D%2F20260930%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260930T080530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDNSl8dFhD3m2nRli8%2FT9xhZTuib8Jaeftyp7yj7UnDQgIgY4SDYF7fPIVuDwg3IeuoneVhh4MjbPWXXM01ROZsBNcq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDInplaGab3z%2FhiuefircA91AYf1hJsNzRvBfm7iG1L3lXr3HRBHpeAnGh4fSPUUdgtCSWYDO61472sikVKEDpbqyfgPnxPiigLyVWldHc3apQGED%2F833AvSDdoWoWwQysdG%2F8jGm4KPe%2BP1DaoodDt%2BPymPJLS%2FU2XR6AXWt7HxjCTaJHosmzzWuWBZfZja%2BO9VN1xsFwvXgxdzEzDU3y0VYVfObFt3AbDvFB8Q8PFe6i3Fef4I%2BEi%2FS4j2veAODPfjGNjDchmDamCDvxoKXp6flyOaEwrRYt3%2FIxki2aQAi46C0mpg6N8WqTSkC2YGcJKXqAr9hUdavgXNM4Cpt9P%2FswEB79P7ZxYscDzmnQSAXvCZs%2BrJ%2Bz80uWyeQulR2mIm1vmcAUQYoVQP3sIIEEXGSiECIOf9D8oFqYAUGlpS%2BNZ5lGTXbMY%2B1u%2FgtUr9v5OpPzrEsMRPNtAsO3xe%2FnzM4tAq4vcVf70eDaq%2B5HpfOrYBlz4R2QbzYDf6%2FMc3yGwIKCjVEcHG3jGHDkQiobnJ9U3u%2BxV7ummszLJ%2F0k4ObIAPqxIvLL50qHv50eC3Vy9%2BBBWrfHTixKky0wBc1jUpoQLlVRhzp6FOqzTkXm8csDM%2FoZjLIaqJDcE3uZeAjFnOQoAqAPpEOxvE9MK7%2F8tUGOqUB9tvO6fwTlhRoTP4HxMlKY%2F7tk4jHIIAyRJrWMV%2FrncVEgqIfSmdySM5fsIL4jEa5jdQLIStXmAAqP0P76RaC3uJKiyQKFAl2ynyvr14HrFkDu4Mp3CYU4KHiPTeopAArCPNXsS1BGKID7cVXfI5oqhg45PQ07o7tOB%2BrLqSbVCZFAmBNEMFoeQ%2Fpc%2Fm0ZpzIoN%2BUUh%2FaMZDwg0indwrhtSCLz4m4&X-Amz-Signature=025228cba1e5c04e3284e37236d27b03adb1f327c9f5f2bb1f830c6d91652e29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







