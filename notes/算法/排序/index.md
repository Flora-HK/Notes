# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRFCCECU%2F20261113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261113T090932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeWKYa1K%2BF1HymTfV1gsC69vgpCR6YBYeYBRskYIHWagIhAPqPZo5ruozDg9Z56Z%2FtFcuX9piordUWnlsxuS96hfcKKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2B%2FtoAc3VZ8dSk1sQq3AP0TLEouSBPv%2FiyrNA86KikjnFhKTxeyjz7PVuMOq4sDjuAvRgc7xZP8LLORc7CHk4MCFjerulzoqE%2FVGwfZfOL6wQxayBmqG9JLew2AGfpRg1MYSaKUyCMuHuWtuXrbSFzDiiaXj9hAc2tvkaa0QY7yvTL%2Frv%2BhLxf5bFShcux8zjMoyrfx78LYG6WQ0U3ewzBuQvA5dVv%2B3A1Gmfrn5z3xAh6OJXJw5jDOgJPtnVWP2O5Typt6BS5qoG0qRAuvKTMGh7f2WUE3q3xM%2F44GCmN2mNzMpAlhQ%2FmY2JCvhAXewP4N3%2F44YKnQtuigwCwm7fGbbb0EGahmb0eubvC7UGIbudoQDRQ7Giv9GNZjRc3Ox6mc9YJEnTluG7U1TncW%2FMd0gzwbE%2F2xvKgePoe9dItBiVoKk3nX8drT03xo8K%2Bd1IvE3XhufFKGArtA7X1yw8tGr7ZDQTrzKy2pPTfd4a6WdI1ekZbER3fBaFbFIWEZL2kEWNdObnZSUMf4NkEjaYr4IPHKx00ZGC6rmy4KG59a0YAny0NtiqvmQzyWnCOhXDK4nIKZh%2F1CFvNx7Okn1uUDmyee6WE9p1QI7yA8zI3%2B8mOMQ2U89SVvGb7e3WGP1m%2BVRU%2FC8GDeX7OmzDX%2B9rXBjqkAX3SKkUyxEOkE760tYo18tS6gLm8UzZdc14KI3GKUy7wyWAYlMyLBdnJieProOx7WYPY7JzG%2F7M%2Fq1KcoQkhpqOuPBVWI99mESmXSk5oIg4Nc5iXUu4vSNiUkd7pF4oPRArGPWC77G4EOm8drktbPCDvKZo7GYvvnSmBMf0zIDNUbWbV46RIRoJ%2BIMq7qjnM65BSxm2ip3iYBbCxC%2Fsb7%2BMU6oQ3&X-Amz-Signature=b247148498ab4f875b032c0d7e995eeebe184b9a22f515dc13303004cdfd9caa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







