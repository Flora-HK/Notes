# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QZTYMH4%2F20261116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261116T090410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB5bYwC7HrWjd6GqKJkFVIRm%2FdYCgt1RW3Zg%2FkFISwCcAiB4qb01W4bhQTs9lkU%2BylmzQfun0VhwAdK3wkSQ6Fc8zSqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMnlHF%2Bk14FH%2Bay07KtwD8XD8%2BK4R39uinGR5sEEWGX5Mz%2BgA30G8ztrt8hotkWwfxC%2BrBfRB1baFXVaroPh8919vE6WwxS0c%2BSEkk%2Bf0bls8MJ%2Fo%2BLAyuUPgBsi0aqPjpvnZyIPnEY9castswBrXx%2FpMWulcOZLJP6gWtmUSlCtPyeNxXRfFEpaGBBC9iBfrKtEJMuhl6QpLNWnHrNWEs%2BBZI4obBPClGub8NXfOTyam0kjFwe%2B%2BYzIK%2FUFL%2FwOOfE6nWAd5DDSJHA1CwqdSo9hmcxuZB9yn5TeZDl6jEUXO%2B1eaKhBVFk9A1DK4GPjGzFwXUJC7aEtIkXSH1Yk7bxXW2bc5fBJeOAivwp9krjDQ%2B%2BWlLVy5M2yIPrBvjAha4Jp8c626iDKjSzadafIMGSPsKOXIiDoRZsUS7LZtia%2FFxPGN%2FsoaV7DEZOPUEiTzmLekl29yWoMjqPnwuEiWzhLMkgbjP69OI%2BwA%2FmQw1dOdxoR64DFhO1iOBhfnYNw1SKRh%2BfhmVyHzkjezLXb7YgA1euhUmnmftw0McbBZqNEUMphkbZGw5TCoRSqwuKNXmppHbq3PcrwO%2FDi%2B51HlKU%2BrDhRyfhx6baxdz2XzsrTSR2WtkL0fM1g3fm9FzhiP%2Bq6qoBa%2FzhKMt%2B8w1LDq1wY6pgEGT2EXF0kWpzMrynwz6oaCH3GxM1tcdmDvz3umWJ%2FHTTjM4pyQigljFS22jReGqQpmh3OjR8o49sWd8Qh3TPbKJXoytNYMADTWgSdFdZl7KFkQGE%2FLFMDQqSS7SgtjE1gEE5fHybyZKjbzygqVScHcwxU9UEzircrEhNAciPnDmVIvApIst7loEbM1zE%2FT0QgMuDlQRsPnbfmCEV%2FE%2BD2zAPMXP8FZ&X-Amz-Signature=0321abd8dc6ca508eb8b6fc72eb180f08228639ee7349207d92f4bc33b8790a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







