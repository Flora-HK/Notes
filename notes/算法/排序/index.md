# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP6TR3QR%2F20261019%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261019T072259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCdf45%2BBiDBr9PUHCLZo9DieKPLtfNfEpJSoluoPfP8bQIhANVqaEgBAQuv5%2FUoMWK9tivdx1lWkpW33QS3lQVwlGpDKv8DCCcQABoMNjM3NDIzMTgzODA1IgwLnha0X42SRLmcVuEq3AODSFXztLO81XqtxltERuHPQvpegC3XRZwX5u%2BxPuZ%2BGeHln5bwrgDF%2FocS9JEs4Hz7nObJyicU1UyPdK3vP6i%2B5UChjGIf0%2FuzCtTRHsKgBv7gtiM1O2%2F2t5TGEuI6obI2OVDrZ1n3ycy5mC5rITKQsEYfbx9hjPRwg%2BPIz26cKyc7nXzu%2BXYE68h%2BxXo6PcW7uFz9HBz6T%2BJnluMiFdU2DQfa%2FpMXdKeQISSc1oN3vWpcq7%2BgueXWr9OaWB5IDx9%2F6gJMO8Z%2BDrXO7zXWHtt1Pm%2F4nD7FAukN8i5xiTxYI3aTS0B8idLAivgXVh3MPobqk25Pic0IaTXBv4IN9MDYt7tRv7ngFPMwb4f6h9jM1lqaMfdkaOR1KKuIpNULc27Y%2BVPL0RKsm%2FmFFJuonUzSNE1f%2FGp1ojtaItpgls0djhGHrsXt%2BGZGqJPKlC41xrU60WN08KD8b2CgRLKhuownV1GrRSeqdWpx4VndieDc3PtgWT%2FC%2Ffzf3uViNDdNinH0W5vDcwRYX2Ok%2BCvv9ryI%2B%2FdMmiyUEL8%2FXJc4N7hE6F7PFdpyGWKo4ZR33vIheQTGxqZj21e3PD2vanb9xNiGk%2F0%2FBspL300IQe5m5iqafbUmRJunBmy14oKXqTD39tbWBjqkAUsqbZMm9I0oGCC0N9qPet%2B8doWilt3W6uMgiMwF5%2F4WUjXzf9Up4e04tFGvjIQ2GXBhXNor%2FdkBZTKrHVaZWzmzJyDVSLfOTQ5Nxv09BiHHPcWpUfCVJ5Smcb3esagRRYhAmQy8BjmHgFimIy%2BkxF0iOb6uXRmIuHcuEH%2FZGqAcCEOgyhiMpJm9jiv9e%2BW692UQHZkFJIT8%2BMd7fOS3WLxltT0y&X-Amz-Signature=39614394c51845161cfc8fc8e89fbf776614b97377ca37b93e2757149e498d5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







