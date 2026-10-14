# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEJDH2CZ%2F20261014%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261014T070939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFTUlBxtZvJTPoH8e8mgQWdwaiwQ3eNZXgiHB6Echg8uAiAiX4yyLOuJliEhnDi2NDG%2BHDCA2xJ1kXU75QY3aiUh%2BCqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnR00R1kSYepRUlOMKtwDdfj4jGeD5t2A%2Bd2bQVsd41D6DtDqiMiomMTSzctJxdvAZwgdEccTdj1HWXJI8FBYXA3PH51fmwixVxhzzgRW4c%2FAXvd2V%2BJdvWSdbH1pLpkxqi18Ouf%2F%2BwSFLd5MQSjS0mCUzoR7chWHLBCTbuSpxkLybf%2FaJ6i4VnmU9te7k6UZYPk57x6V2%2B%2BBek0PCEcSLl80%2FHFM8Ev%2Bjk3VGH4ndw9bvdLAEKVxkCicxgtMqzWlRugSB%2FYBmr4vuutR1PPW4Wzg%2BaUTTJGUTTH5I%2BDNcTjwfgw85OfEGTQPDEeDs4joOyfVUBlmV%2BJ%2BBskLR5H13SZV7RTJyKT2MC240322klZ77KXjCXNOtokE8%2BM9HZHTLdypf3twmFpmdry6vAq%2Bp0XVorDkL5IhjPRlaqSSPXz8NT3qbOvr5qHV3YpK5vTxQoexacnNRvcFtmDsc0N1%2Fc%2BHt8IDO10Rf6bhupRcVbeWyrfE1oDogHWA%2FihjtgLV3D%2Btzqtq4PNnRtDUXpt99G5N9%2Fy8dW15iWQR3dfSaTP7GM7r27%2FZy8P7xTVgDmy%2FQXcekzR6LtnfSOqxxf1f483IW5XvAyozXuxGh%2BZBakD2C5oqoKCBiZSJeBe3TPU9iEGDHRbb7jjPj%2Fcw6NC81gY6pgE9WdXQPBchZDF02JPHZUfIG%2BbmGU4j1C1fGsBUCdYL%2FLI%2BI2ZwYoq0Cd5Lp6pbb8vX%2BYv7izBI0RICcEzCw2fbft9n0fYj8W60Wor6efBhLsPidNl7aRqzRCqYhNOpwl7tk%2BbG0hcZbnqsL0jWDA4oYBsPRVKFJl6r7aikFyr5aI7jvYgqzMaJuZsaKb43NWbpwNVx%2BlUdR2MqY7Sczqiq1zNq5mY8&X-Amz-Signature=f77c38ee2c773bbb0bff41a9ac816574717b984c0cef59dfd0e32bdf2eb14abb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







