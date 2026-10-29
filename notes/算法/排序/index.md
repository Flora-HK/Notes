# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNB26DRC%2F20261029%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261029T080538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJHMEUCID3kFcsptY89Yc4JMHP%2BBkGijeANHKt%2BiEkUz1Rw8JYZAiEAjiRvq16GSSgBrMFMSLZw63zlVDVXQLtaVO8WtVJPI6cq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDAf65QZ2ifYyUCTnsircAxxr4hUzcYgeWEeXgzmfR4xHEy8SVbZFB49%2F30IaBkRcFesiONLJmGmQoaELbGJMyr6S78ClOj%2BZ%2BW%2B5hciViYJxUXt3guYjdWDQ2rTeGVLWGq7JFSlKYAnanhDTUP8qF%2FnEPNXfsbV6dv2pYcgyWosDArrdAfS31XV%2BDRDgS11Q%2FDeQnxLKUWSNYni4GFq9leD0GPpUARkcBc%2B6huoFTZBum6Ty%2B5AblTxkv4UW4kjKQrgAPSBhS4LvnEqAzps9TKSOReazutMLdpW2SXoqEvmdOvZu86RitFJSogyZCPXMdNPSYz%2F8y5s7naiv5epuUdH1Bqppot9CN%2BLIRqJjhzDNr1itaZox%2Bw%2F95Y9TgXrMwjNLLpH559qEMsi44WtvetIrUj3GeKixWM48PUtqqKnmSKt3lcyftwYV0%2FPGZNKVpSSYOF%2BxsN%2Frb43Ss%2FVnqSmiR0hdHNSyFn01ppLzCLMAXKqHS07CS2FuwkSk6zrbaHNBeJn08oKmQ2pDMktQe33kJUWAVqQkt9fAoRMnAAij2AU0O%2BGC97uqW6LDWtqAFCPQeCVCH7r%2BvWVC7b%2BHYSqKBJ1ZJpgSLdqdT8lcDJvrg6Vd6lJYPO%2BjxNwq%2BSVEd6zhy0mtkErGtMLhMNK7i9cGOqUBVSW4UBTxb60WLUdMHbjzX%2Bs86HxwHgyXCnwkqZx0xRxboFvk6rzscMt1Igygn5jDrJo3eMaeRj6662qVDzh50dksmqNWqVH6g%2FF4vRlQnDXA%2FbV%2FzwWZb75E9CcEC3GvDTlJnSzY5IlExwowzA6PS0AjNwTk3Nwo%2F4ebKjDBBqY3NrCYLife2JF82hMZboMvjnzTW603DATVYlYoGfgWjdQE43BH&X-Amz-Signature=85f8d93f8642bd5ac92d53c4ed52043d7b8feec6e67030d4e2cfa5643bfbcaf4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







