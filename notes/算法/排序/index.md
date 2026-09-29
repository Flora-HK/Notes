# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654OSJG2R%2F20260929%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260929T075627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIBAep88LlwB8emvAdIRhlwvFyYI4%2FQewmLKtNGSyBAvZAiEArGNMVv6oe3kokC6VgSZQsM65zpjC6n75yyTLQx0gXBEq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDIcYoQsg6RYC3b4YjyrcA%2FpckXw0R%2BsDbyTxVFZljFnB%2BTbA1D1ZmMQpUAgotLxztu12LyR3t66YZ6%2B0R6XR2XkrECEJrSFVyXnVP3tI6elml2ouuX%2Br5B2V9Gjkvh4FV3lnLvCfProjKe%2Bp5%2BUfaHwtdDtWjAIJel4266m7H0Iq4J3OeOPXA2jet9BGI6pGrY9lVlg3MQUjX9mnuxI8JvnPtI%2FWyXNsYE6GXtAZjmmu64q5bD%2Fw%2Fvwn2b3Yo4dVxoZSBr92erlkfA0viofa%2FpTJsarMb5eRcwq1UBuYEmeckh4EWfx6qI6NaZLIA1MS3Tia4egvTbD3wVPm9JF9SgDtOLZlOWdsmbz7oBferEJXR652eDB%2BrN9hOBYPb3nafy8SZSrQd2wgwstSlVW6OT7iWUp16WnODbgfwQ%2BmfFukRx5tbLINEiDkFYQDD1X9I72eWl5KOPOe6pxcHQ5YDmpyqjXc5sGX4GsWF1PD7mRdtkKtX02PAxOUJIARntvoZhkQZgfM%2F3m9CknbzsTXYletBA7VMiFyssEKun2vZhwDTTs%2FKbod6DssMK3%2FZHTdGQbosCBA390X2DjYqMKGpABximmWhCzAYlGVu5Co4kdM95Z1ow8GdIeq%2F7dd9TiLBtnKuls%2FR6y8YusdMNTF7dUGOqUB%2FwETOp0hpxYr6MmAfs4WBUHSxrX%2Ff1i49oe%2B1gYaRn%2FJ4wvcYeUPalM8Ds44kwMv9kBuoxbMVMhHnsetPdNH%2BuarfZ37HFBx6IVFqrZVB2%2FuSylA8nM714B3yAsIz9tXglVGG2vApRI4uzWQtU43R1SOz1aLEOK5QkcsCHcgGp8GS0OllgqXtLVn%2FxsJjiXXs%2Bl1U3jy%2FG%2BpIq3LjlXdWMQ91WKq&X-Amz-Signature=f50d13ff9e76bd43dea701a17bde158f40881313a9d0b49ea90e547d9197de10&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







