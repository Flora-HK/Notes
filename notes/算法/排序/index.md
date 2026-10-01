# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZENGMMYR%2F20261001%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261001T082318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClYEI7%2FRBExEqW6DfOS85If%2FMXDUnLCB4a6a7n1hWPAQIgK%2BPppZEwn3pWt%2BJew7JxVI85QFIVse94DwS352PACiAq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDHYorxfIE70ywyEBwyrcA5V8Ligz6jSkn7a9tn1Qa%2F1sZ7U%2FHcZeZrDNc7LjauOsDM8CaqqWLdf5eh8459ByI2xdWFTq7s5hdbNjk4H6swJeaWJyBtq0SnqU6hgVwaHmJdt%2BHb2Yg3qE%2BBtDIslpPciA0yr1sHeOjeFWOIdcGd7ZYVPvnWvgNfNKvl8HMDCpVHHcF7yWt0RyvQnAay5nZXt16EL42JSUeXxD5H5UIXBfC6plNdWXpa3m3qQlqbJqSKIY2ru%2BvcoTAhACHb6wYj4UpjhB8QxsOkJrG4f%2FzZUvQvt%2B5RWkaNuyWrZ99RsR6DybOAjcaIRtgWytnxPl4WLHGX5%2FqKcFDCRchj%2FVmt9nQ00blDIgeVYxLI7X1MxgpnEiPv%2Bd4k29BefUFClmQHXYIMxPJCqYpDvcZyE%2FmJzqHgPS6N2LvA%2FfCANiUoub5rfRQYHuHyqJ3qF8xgGu3BTWc9fkHJ4NhDRqQZN5KbXs0cjE5bPan%2Ftu%2BjYDo4RbthSWHTS5Zf3NP65Lsc9nKs%2BOlQI7iK5Jn2tkx%2BasW5WPOtiTnMzhayAacALmim1UV%2FBjONHa3kZP02G3z9Rzkpr3rMhESNezXTBeAhd09birEZh6YFYYySylWlnbI2myUbpwsa4urs3R%2BZGvMKSv%2BNUGOqUBEYZXX3D4HNQdjcy6rqF08sF5mG6lZgMxsbVGcI0hiD1R7GhswEOZN5wuRJsiNP6ka7vYxFmoCdwAf4sGouFwfKpyrVPsYut%2BChiEOh2GIUpWzMngZY%2B6dffVKft19g%2FZAvfZvo5si1RnLdmw8ILp%2BmezGw47RHuKu5a2Rng%2F1rGuckseEaj2SoxRP%2FIq8Xm1kur%2F9PyfmPjDn4FsFyQkcYLXPj99&X-Amz-Signature=45fa19237e5abd7d9f184676e574d5db7fff6aa7150dc033a3e79605a2b0957d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







