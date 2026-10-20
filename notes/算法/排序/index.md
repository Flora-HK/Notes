# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKOITE6L%2F20261020%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261020T071338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCgvDfny%2BD90CVMw9kCaE12HMFP%2B%2FCzcmXieF1YHWgu9QIhAJKkg6163JXLSvDtfOaaia1SL8TPLghaJpKqOKBaDm3HKv8DCD0QABoMNjM3NDIzMTgzODA1IgxTKwcEMG2n65y%2Ff%2BUq3APVWBE41ISQISX%2BNhXE%2FnIUx0vxQ6CulJXIK2RfyCugtT1DnrejO3vDXkTcS1q8xxIFcGelcNdl0D51TaTJ4K0X577fu8Ja5L3YtHWotNeyzqatukrMghawUxkHBhJDZZOXuoPmbZ9QeJprYUZucBczuNZXhUQBP17P088BHYhHiCR5ewhkHhv7v2IScwaHTtj2LCtI0egn9nja%2F0Hyqun9lnBxYBgpml9R2S3MLmsPutwz3U%2FzQcmYpuvTc0sc60Ldu4gyBX%2FwyE9AFsyhOMBzTwUAhIMTqIrYw%2Fi1LmLYm4jjPy%2BoGdYaKyV65%2FAnUnFW6aoombYNe%2BXXhp79ZQUiJWX7TV3nXhgw3L0QeHJdE2pm8uhHHf%2BSrj1LEfiYCwdNAWcNq9ZDqnHt2QsBsz9SOpSpuo7WFizCiZ%2BXevcg6c%2B1JIUL%2Bx98NpMkxU6e6tA5ixkKswxIncIiV1Ndz6HgMf9i1akq14y%2FwTMRmOR9qDmawU%2Bhof95ggG3rrzAE5x7VNfew8kQmhxIC40pq96bTFx%2FFPiijeNsppbv7iZQncEjJUmQonXMsQ1X9CqUG9fExqSqUmlKo6DY%2FNdGT%2B57j9m7fPF1QVj%2F3tle02BxRizEGD0svO%2BSOlX1ajDX2tvWBjqkAaT6EO%2B7oWb32Qg5vT9Jref9ulDdK2cdlfYyY3NrA6zwsQf4KX1o3K%2BIlFAcPCbynvvoyvw1Vja0xAZW1%2BTipvv5hcvhsfAee8LxSNhDkGTg%2Bt72mX7tmE8mb4ITIqotaPm3FBMi%2BPTzq8NXPeH%2FTwEyrc3ClarOmZSqa%2FxTjgvX4r8CbUW5%2B0tf6jT45%2F44bqhF%2FJTuvACzuzLzpbvahPlOiyde&X-Amz-Signature=68ecb0bfdbec6cc69db750a35f26ee29d7d33017eaf9e56fd0d13ede80687ba1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







