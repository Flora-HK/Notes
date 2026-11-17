# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQXUBLCE%2F20261117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261117T101607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIBi4y2trdlQSFH93a4GWWYzFFH91RXpM4spbYfltncKIAiBs1yXuMVxUs9K%2B0iEzJ40vAxRjA1BYRImhMH7qnN1k0iqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrT%2F9twPjsDXVjWmaKtwD2bzq4Fz%2BU0disNMzuvnOVfZMfqC3mVoy7juzEYAqvBD7UkuLH1vATuDOxCVK2BeNYeiqH2OAQVYQ1iZCngkoWUA7QpAyVulmOTZwvQmN20B650zZiIC2gc%2FdmFgo5%2BLLtlgZdUH3zQM7GKj%2F9ddbE1xRuZUiopuwKdJyOEfwjMUJePFMh8LZ5iLVfouVB0N%2BLjCWkAfq6K0IQobBQp5kBGO9XAqzN9ceMUG5kE71H57uJODRVWpCGowJGIvwHJE00i%2FwpYUibx5ZYIrt1O8HFVZGZqtrZj7r6%2BKN3A1iTrnN1xtdkfRECUlTZvT1WEbziueRgzOK8pwMQhn6WAoD3xh%2FT6ryc1UFWUgLYXVclIJtyeDEZntVuNhMB7wpssHzqR38a5hHy6unCF640bGBWtNrjSWHWnVpV4RmfCB2iRNeRbWVFJ47G%2BLwbYkd%2FQLXJIA3a3FbDq7pNLcbmW7bj4gdC9e5SZ35MmldLNbfqkV9bHqENwUClXQGGb4KrupU56m5MZyrgcs0rA0Escjjpjd34Y3yS6DGV7%2B942UN7oEP9fQwmysSpNqwgx0aGhKjq2cFF4ehXYHgsjYBpKBy1uWPL206E%2BZ422v7cEmp9RTJljDmUA9XGowbtfwwhpLw1wY6pgH7sU1jtiBYLP1cLxpwnT9uSugg5SSzHLRMzW805ONFH34NXy5RoQSXLs4BkDK6i0BvWkUylR13UDqlwCoV5mxNv1Fy6NM%2BJaV6oWdOES5mGjSBAcBZ%2Bl9odffdSCj9mN6lQ%2BIUo39oR6SdVZEXzf2bb1asu7eXCNXWq24UAzmj2XDDfYdEbbAoGaq5D%2FM%2Fq3%2FMfeUX3S%2FB%2BxM2CkA0vJi9CjquYEad&X-Amz-Signature=fda623c2f17366aae4500fe832441c71d022fd397f3e5780e48801dbae551836&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







