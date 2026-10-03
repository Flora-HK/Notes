# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRTJFWZ7%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T074021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHSrKcv1gv9jotqbaQN6K9FbOYb6rF7%2BjicuV%2BW6VKFQIgHk6JSVmRwysQI9Ihl2Wif2DoHDkDU5Z%2FU6BQ4eKJ70kqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOxZLfgvU2Ib9TwM6yrcAxJZQCHWzkACyFpI6q8zHOJCiEeVNejqm2QLE67%2F5yxyJyxZnLE2%2FPf%2F4%2Bre5SRGFb6mz2K4iff5razOK9nBvaNOVnTW09uApW919nX%2Fzi3At8f%2BBsvc7GhdLm8x4ql4T1vSqqg4LjO6y%2Fe7FRFCNgs3%2FLiI3AJ3srGA7ZHa8BVBdqUT9xfip6QENTAzk6P4h%2BYSLHrp0xWgjdmELyTVeAjT9y5RNpbebcswwNMaedNNNxGI7Vik%2FLG8HgIWSLV9dZcOdH0mzpFo7pepWOS6NTDwRCla3kdzvNIVwr6OQpdcg5seEwAK0IPVa1%2BVXP3Owkk5mr%2BfeQr9WZr5OdM9MTzv%2FRwpvjBDXcjaEUcfgQfyVIPviEIF8eg2D%2B2rw0J1qoSO9OpjinwUOUvx0oLiwZfLk91tqEaoNYiufjCVQuQqe9ZrA%2FELQyrVrzte%2FEvsKi%2B5YBtuVT5VBcD6siDKe1aimK5Ip9dMZWP9H8bI3w9GbKGAmDnfYYbvn360keClQ1SG5boYhoro0r4%2FMgS3VuXv6tFO%2F%2BQVs78PEvOKm9rBrEQPL12OR4NmaSvtbztSzLqpXZWxfxeDoue1tv%2FzxPtBo7ji%2FVqturZjbPKIoNwh2PM6%2BLOAe92TxYyFMPS%2FgtYGOqUBTsJIX6H9EvgAvqUsQ8YoppeAXWpWpbhT7YAutnbBfxUJA87g0VavGLe7hwdDQPfguxzY5HeRfitc0InL4rg7iegTIcD5AAZmLjm6e2jBprNX0ejcUHrDSnzfzigb0CtSsqFRMDT3kbHx9T2mcybHO8rC3CaylFrZVdPjjLnTRWdnO8CQKcosL3%2Fu%2Bce1SRffi7QKLJJTMyrGBk1GDztWWih1uPOZ&X-Amz-Signature=183f75a36c290e251d08ddfbc490747b0b870db8adc88f6bfeba70b1c324b40a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







