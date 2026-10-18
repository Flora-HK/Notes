# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BI5SMED%2F20261018%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261018T070010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIB4kgNIWxyn06zeE1Ec9%2FYjceN5c4Wyeo9cS8Up%2BIeG7AiEAjZPGz72E8pKylT2%2BcOAoJHvH3GuT4T7iUM4EhYL0pIUq%2FwMIDhAAGgw2Mzc0MjMxODM4MDUiDEYj8sglKcA3FZakHircA8i8KHtdS8xzVigoIVxxkkvEWdtta72l4WCWfmDwOUTdqCd0ZWstxNFE%2FSWY%2B9X4%2BylNiBfWBSdP4szmMm8YJPFBXCpJkUs0R1At5uuBx60Y8Q0t%2BIlSFVINl5IiUAwhPgqZktwEIda14I8DJMrtFQdLl9%2FSNXo0HNqEj%2Fzdk7cSVLJipOSLV6veNj%2BaQhWZ3Zh6menvadS%2FQpNfCUGt7GC7ZZ9qLOMII6D3ikbQ%2FOGYaQJurjq7zCkJEhHAz5GJKVasl44nh199DSgEwfJhkIfVkZV5wr3NPvWcriEf7lNJqhtZiDI3BdSBeXwLG%2FOj7PALkOgWutNSbI7YFtBIRKOvBbJH3GuAWMrUEXnY367OkH5MuOWs%2BP7g9v%2BycYnPwXbhQsP65AjlSOVtBNmE1oxEjm7SqfSIwO8HYEKyFhomtN2PKYgYM4vyMPQXISsLJ8iYQaRTCWOwgmFbKygl5HOCwVWeGv6e84Z6EV1rtFZ6VabVrCsqX9n%2BJUIJLcBR7CSQCJ4VZDXm7NwZSNxA3rr2elDdXMLw%2FVdRlRJsMc4d%2BHiPLJkGS7Dvg2pjDQcgeidtHs68zCDMLtlFb%2FJH42cTLITv77VU8wQsygUQA2DH8n5M90uoBIRFIUukMMLA0dYGOqUBbjrHhhAZneWYJ1g8ttms%2Fjeln7P%2FhwtwiE3E0cOvqza%2FIBEESuVuJ76cilPtQxb%2F5oAWfAX6Z%2FXN6GFZgAGQ4VyrRq4Rvs%2F4gZtiMkI2gDiidZH3lqvhxivO7cszBE9AcytzaOEBeZn%2B6CYrB15AZGN7cP9CY18mrsI0VXa5Oq2%2Fkv5QEv19Y6auKmXt73OmmsrvyrMEUxoQImeoD87rRki0P6CF&X-Amz-Signature=4e3a012774a577ce1ecc1d74d8bf34c65c1c0860b24d40d0f32f3a5f97370b3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







