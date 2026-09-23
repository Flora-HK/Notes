# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LOMVSJN%2F20260923%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260923T072531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDaeyvJv5HcjueSgL5u8MiTHKsR%2FqMkT2CJ7iJmwCGg4AIhAP%2F8%2FRzs%2BpU7FR6PARBwiSSBxPM6WqCsswrLA%2FGu%2F%2Fo8KogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsWWR48HTBw7YLE%2F4q3AO%2F%2B490BXWPmUSvCpdoxWbfY0IIs%2FGWxKLnOnCzO9lgsUErVEEmRxsyezRGDOuxEJzCdVfw%2Btlw1XL%2BbBINA19V4nG9kcY8wZks8ioR82c5UnAhfZG5qvspo%2FrzAGnFnvsrtKOPU1pUmOvR%2F2hOuRvGXpCt2wZLNAppHlq6E2eZVSxZVsDbd8KTt9tLsw28y2f4qKVCOs7I1jGlYktHFpjSziyY1rUyXfIKAeUxVhvDCxawlvV%2BxB3jowRoX0yqrj%2BUcALh3qxhpTNzFHhGXu92xXt%2By5%2Fcoqwi8S%2By6W99e03yOIHr5ISvKKqLxUQtobonOmHukFjGOxRgp4ptfB4hRr4ZmSideWfXM2c7MfQkJH%2B7%2FonaTCYOiHvC6C%2FtjCJHzO1A1372LGL5ytOX5An1RxLNEwLgLdNx4B4IviJvwN2D9Jfvgrze1uzFVdFIfwCHQVGIIzI%2FWVuiN24de8EyinkzBL7aWRa8Hp%2FxPx6MuyOd18fNTgPrvTmfCvQH%2FB4MDf%2FKQv0Pkuw2W9zJ8QBYdyt1ck9buZs7DHb7iH0AmBqXFtg7oODv3pc2eUaoRDl%2BXj6a%2FmxiDxKX8yRP2d6GY6zkbk9V7JcgPK0y4uvnvZfK6081eqMcsnLSrTCe%2BMzVBjqkAfQd7akHs9El9%2BuwHhgSuJovSGiaDfwDr7yD%2F1v5ttnQVvRqfZ4ps1nLkXMC1Aiz%2Fy93nzfHMD7FG2yKAOyG5%2BFv7682OWuQ737kYvbHGzDzs26eEbYNP7jo9rS2uIjWNz9ygqZIoF4UGwie1N2oRNbwtj013YXK6mYF6fkCfElM%2Bt%2FA1mJcRxkEpkbFxiedWGzZdX2K9nTRa9uJCcCGBP1b17cz&X-Amz-Signature=3dad47ebfd36c069d6a56809bfce176c7d2035fe472c51360b21b864c0c10c43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







