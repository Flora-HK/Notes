# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPJN2NVM%2F20261127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261127T103459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIAiUM%2Beb2UrUTUXpqPYnCYjjOj4Nfm85ptKbOvwiXEUeAiEAuqNyYHjf7GCIFZeWvnWOjjk1aVp%2BsGLifCRydoY0JY0qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPep1GgUZJ%2BfUDs3aSrcAyBwpoOKa3XxMnWpRUKFh3LSKVLCE5GYOrPKXg3ExvGHqCUoll0b2g2M%2Fm4SvCbZAoXlD1JLvU%2B6rPsAHxQJj3bmcmCEkhWnKumcjZM2%2BMkKexG9oonSHWGu7gUzLGL2Cys9MfxKiQcuXJZNHNmGxBMKExfLthh1h%2BdAIML6OhElcdyHH7n90f%2B51tYfZewDkn9LAyOObxKfIVvKWr29d9LDA3cCag9meHi1BFOJePrdwELwZK2gQ1xsWPApEj96XHIg5OPbKE7w96LTHgEHso7TaWNfqyNBhlbtLGYO%2FXRuVsrn%2BgY8CmFX560IeiNbmX6Fw8asrJLznBsGPg8PX87yaqkME3MsNlE%2BBvMA4%2Br8QbdehSsPOSLGnTbLCI1k72AgWIrS%2F0gRtIc9%2BwH3sAX6uSmGUvUkaW5BEt4YQGnqS6meFS60fa61IZP%2F%2FAfUMqJ0W5URBS3LbFJu%2Fp5Vt3S7l3s%2BtN0dvfn50UaL6RGRIMoxrJW5uw2IiispN6z%2BorPS%2BVAIdAXXL3HZJPz4IANFKIpIdSc9DDJOgSIwDysWhuSMXjILhf%2Bcn309pqvQiVK%2BwTnMssnYRmZrbHzAWhxB96SAIAR7zw11UmLINpTCsY2DN4Wtu2affpGpMOWDpdgGOqUBUoTMECp%2BalglDr9lMR5oMV9arl6f9D9pVJSZhYjAQFRH%2BmYMphUcqbeLFXEbW6qQyjfqDT4oP%2BMK2a1zN1VfE9LSCS8GhEUG0xyAbTFLPXvFlfmOEih5sk2cRz2IRVG6eLkqyEjZN7n2ODXngIooOeEOykxutbxm%2Fx8UVvNy73DYpw8eEjxGBn%2F0lFlbL6ci%2BOqWQvRJtp%2BCE7Oei2UIqbqGYu%2Fe&X-Amz-Signature=e8b5379a715a2d19597d269c5be9f942d446728198df8998547426fbb089368f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







