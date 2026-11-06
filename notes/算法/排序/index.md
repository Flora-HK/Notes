# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642IWDADZ%2F20261106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261106T085752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQD7IP08y6sB%2BjpYrXGMboK%2BiBpnoiXafNaC%2B2gQR66V%2BAIhALrPLAcvB3r4DyoZ2ed28tk2ppYM49bbyoFIM3ECgQ%2FhKogECNn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy5FaSWbTrAop6dmcQq3AP4v9qZ5rJZDQPkXXIs%2Ft6h6yuVPTGU6JFbH9ehQntNwLG0tRN2cfMjV6qp6hbUEn44iiWthYy3D0KxAUr7ofDkxq1NusPb38uFaWDoGR8EveoBEd%2FhdJgOl6r0bgi%2F0Npfx65qo%2FI1Y0abPWbvcN70QAjmvjI4X2JnoxHuyYWSaEmfZXWTWI8Qa%2F%2BCoBo3hZekFog8gKjhBnDFRU8TzcchghHzGoeJsqdGTjhf0jmd2j4DoWmv4JvY6zAlmF3OkHTFoS46x%2BCpBF55dv6j7cL5tV%2FUTQ6xdtFi4XFytCeV4SqNvHHJ%2BaMKrw9fYt%2B8PnnEtgEEl7d0VUzZEXhp2pR9sfcO6VspsE%2FbNikzzSkpcyP0hpIIHYKhw5JZORQXHeKo62oqmvEK1Vf0JlTmeOuyGSON6f%2BtSkKFQaAI7Sj4025U5NSnUwW2%2B4N2DIJ0dz2AaDM%2FRoTzFZR7Wf0TdXk%2For0OyMzmvYcbsMEPlAFD9RIPHOOc20mAtcmI0X8Lnp2c3Z9UeA0INom6WyV03M2qqM85oULU6bwtqNiq0%2Fc4AOkfxB7Dh0jgk%2BfJRKtQf1tt2J4qBgQqAzVn2M3jUIZQzmh2dsGq6%2BSli9NynIuSZRJ6CcNH91kIdioVkTDglLbXBjqkAeRys%2B4nzUilfGFqzeuywy4WIDeBjMfpXGG8uOD%2F2XK3PCnZ8gYyMOdQgUGSsIAD3qapoIkSGTwYHbwlli%2FoV2WAS0gXhX5xVmptRU9KRcZpvLZRuZoxU9sGcZQftNywnb%2FAi1GCFG%2FiQIlq8DKNaE%2BrTZDsDm4Nmqnn%2FNG326d4QZrW5HlI%2ByAoTas9uOQHyS70Or42rdVsTY7QbDHZsIQ%2FieXq&X-Amz-Signature=c3946d30f76ca4b4c6061a1c1f27e3430fc299bb7cc2bd29106aa3ed69d725c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







