# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGPFEIVU%2F20261118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261118T094752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDVW%2F3InSWfpcAWB6uiGtkJsHj%2BppK1P8BXXMlaeIObgwIgbW5D57uuoIH95YyeuZm45OhT4mO7OQQPPSlDkHNohaUqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFAuPCtRZ8d5uJKfOyrcA5QJ8S3qQZCo9GtQTHHInxCNoQ%2FGpzwXyukHzU2ChX%2BELWubSZhr257ul%2FC6EQl6qiFgeAesYmhDfxXlbSw3fp7KfHRNBIi2k3FMjXzw3UkFvhgSyhJfmAmyrDtZB38MJOl190qJvW40xtPOwGFqCz2LdAdyWnNkS8GwQq01motbM6zKvEplD8MsIn1OMWKy8FKjPgTNOZl9AuXoiqC28Quno6rrJ8a2N4JPEANAjHYl%2BS21RPv53X4XsSh%2FGoPsWIKHfderpsFESF%2FWYXu1ENhc%2FGxIvEu59ixET1WeitpzGgYeBg4%2BpobW7WspXGk2D9JlSiCyRpvYamXRPN8lKIuHbiUAZPjt7x9I0Pm30bM2kaHKcUKSvKr5YKON49gfVv%2FuXgM%2BlDz1aqwpE0Q3j9VEWRaOFbMCEVBaaqxbQB1sWWDMTtHEUKEDXU1giZsXvDm8luR8kzxLZ3D8mibrHtsMkWKw1eI6OY0YY36EP9WXpCppfDlTqlbT%2FeebU%2F9Q2j1S7fx8LvoyRHZOV2L%2BygT6d%2BGpYFIf%2BiwLs628c4VVT9RmiwSalIJLR4wkG8GuruYw5PPuhJa8fQbYcpEOmLjuAvROIC4k7GMVbDYZUa2Tg8VXY%2FXUw0rWf%2FiZMLHV9dcGOqUBJ8Cz92VCFAF74%2FzBNTuN3D2HPvG1uIc5L6gsbcj0eVyT02DKNCiIescEmZaatfHLilRN7Pjs8gJ9ryNwYWJq72q4Lx7Sd%2BzNNIs3DV0z4R5y96xIYoD51b2M8%2Fq33f2ac24dPwYSFx%2BuVShQ1astbm1eH3R8TQHS9iwYVvOswPLYCG7K3RCUc%2FP1Pv00AFTbnxAviKM31jYIltXvIh%2FBJ9j%2F8UUR&X-Amz-Signature=6edc577a9c2077de0aea174d0a2f2d2e3bf322e07687368d1523e65acb296b6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







