# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDHFTIPU%2F20261015%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261015T070143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxKr%2BJFpb0iUjesMF0asu2QR%2Fh2WcRIa6Vn0UTvchtYwIgK1a0X%2BO1doWm22q18IzfF64DGnNknFrzqbO0zdRHTrEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2BRH7qalU5xAnx1zyrcAzuazSaMe328K5B1gHvHgar5eA2RP65BYkXmUOCSzyugBj0BBIgPQSSmiyC3R3Vr%2FP4sM5GDkHt7DC9Hh9Go%2B2Gg0WACq0F1U4cfA7mf4DlmmIKI5sPBlJ1TmEDwpqrqucL3cGTfUQbmbht4pTsxgGCIYK%2FwJG1FF3Ewdg6r6yBasNU6%2FuTxdjxmFzYTi4E5gkIOZ6BTxUgI7UPihBC6syfsUjgjP1xbSIvIbwF%2B01CgucexjJBqQInCxjljGGYhmXI%2B6ye8QfcsOg7k03JaFAC%2BQ%2Fvgcpbm02coQIhvFxrw4eyK3o1G8nNEytTyfA7paTqciTrQIKIT8bL16%2By%2BD6qbsDRv%2B7YDXBvw3w8belttyppCM7UTuRz7MA2ZdXvHLwEbX3hMYTyHQKo4nqG3sRs55%2FOva7c4L5mDzDdLzMnOnGdVjEGqa9cXsUcJcBXsbgMp5v3yN644U1lLkfNl9lNeGvMZQ0OUC9STCytvhSUREVZ8YP2c9tviS1yR9ELgrKzZB8B0J%2FMIf0aEysh1WLZAnr798okWmYTJiv2Q5kEK%2BhJfynU4Hog5ub%2BjvPxO340%2FKpdB9R1bAd7rmHZgxDhasslBp7S0Un2pKTbNBqACkOAGolB%2FftiPgqqIMMnSwdYGOqUB7SFowDt7vJzRWeZq6qAKIV4JV5Hy5qp5fvNv3FJ31e4TtIIfxYsiR%2FVma6FN12KhoWMUVQ1B44Gxp8nWyY1ieyUkRCcg9NRQ4TzD15pZhybR99iVJ8Rvjk3DzluBI3RGvjKwLuv1%2FTQtc%2BfgNVGaZV8qYw0ZnqvkJk4IpJ7xctk%2FkZaEOhbdG5xKsnERdfJ8na7p8ntixVFYVlFotE3RSvZR6%2B4D&X-Amz-Signature=b5ed68aa52d222b896e95bd0b25f7074ada505311043163d92c682ed70416c46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







