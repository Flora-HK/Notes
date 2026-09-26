# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUHJFVJB%2F20260926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260926T070710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDYaCXVzLXdlc3QtMiJHMEUCIB%2F62daE2ROBWpTR8aSkts5iiVIZuRD8nukRwR%2F39BReAiEAtHNg80LCMaEF8WRE2fVImorACNYlpPob03myKZTs%2FVUqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCIC94BcWDzTTYIkYSrcA3gECy6edfngwYbFK0Wzv9HMC4LsmIUXZ6TCJyH2B%2Fz6%2F4795fgsJzcb83KPUoKIXmpQx3%2B3J6NctxcjIBH3GU0HUKdZZ%2Bpc6v99bpDTL2PYiTpUCieYBEmAAlZ1GW0amaYk9PTpQ4SqVt6kUGiuD1WOl1rwYeVjNF%2FAl8QJg4wAeLxEJ4HkGwZRLYKKb3p2Nmc7P4tDMFzFS%2FeQ7aQH6z3wxbAhF3286mn0zJz6QJmAq5fuU8KP%2F6zZoKzKBL9fMIsko4MDn0gHGjBhiK84c1QTLsGcLnOW9Sl3KwP6IwNerOZgwexM2wMVOV4x%2Fix9qJDs5btOHBRbeO%2Bc9KBl7kdAc1%2F8lIqlKEZnZeyh%2B0821va%2Fg4iStjmqJ9DknpyL36CkcOzE7w%2Fuf36q0XevZn4ZIbV6nacKe%2BoDO52TJUblYCmYLdaxsuFrd9zNE8j26s%2BmIAKJOtrkDJJ0tjoxOYw%2B75Fjjuy4MXf7vGdXKCOiLTTL7%2BFPtWC5maUAqnenyWtAleqIHQm6I9%2BAe4C5fjVmT%2B7a7ZMl7jJ8EcEP8M6gc7ZiCj%2Fdy9kwIFSWdqDN79CRuqXkgRxAGkIs91NvdqVv0rhMSkMXHWk0vOl2eyR5uqf7BpcrNSHP7yxBMMbG3dUGOqUBmb%2BFWp%2B1L5Au96WhOrAwFclHEzK%2BWTYj4M5gQrSj%2FcpQE6EYmojVAUlJdRzchf1GLOwOuWLw55kxJfMs8MGeeeAuVxLKpzM%2Fs5Vj2bfuGS%2FnwH%2BRCH9paKevzyjVVeM8OqCSbnkB06Dti%2Fae%2BOvT9TIM5DF9RUBHP2X5UpC%2F1nfgnmoufIdywGiPoReRwSizjKYMU6E0VHSWcIpc3eGjEiLR22MQ&X-Amz-Signature=7922c5edc6e2e13cb57a590834c514ae54fd0e485896d87d2e43a58e5f243d04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







