# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEFN7HSH%2F20261031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261031T080146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIEBS8mJ1ENePFZPTrp%2BbgEqUFwNUMitVH60tGYY%2BntrGAiEAtAoANs1A%2BFJO7flYmWfGTqlWTwsElP6Y5tB%2FXmhdwNkq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDG72UgKLZ5bv5vrmJircAxa%2F8e79%2B%2FsyMLLwzQayVWet2vIYcWowsIxsSvj%2FPJtWuvZskj6XblfnIbn5%2BehoTEyJwu37XxQGdlJkNGRtXJzmpH3lAnz2QMPT9Le8dkb1308uA%2Fnxh%2BCI8ChRwXj5i7JzcHYN9SS5WVSoPyFBR3wWe317XIqKrSYZDAUctp6E5M39OWj%2BCwgmxKBFqXEpzZcwk9q5cm5W5JcIg3mpXazLHXCWTVkoIsZjszsTMbazgIMis8Z5HOxDr6i%2F6Jkzo9clqeI8WdtYBbMLgJq4Vt2zrHFQUVsW6djAiHWE3ICLMd2BZ996OA%2FNVeYTNXFNgjRQeUL8hjHidkPH9x7lWUGdV59URyOX%2BpGCWfVuCLX3%2FItgOQj9ZmlILODEQ%2FH2ZBrfI89TWMAALYtr4WbJ78R0NAge%2Br2arZjh4txFCFOxeHY3LddMUBwy3vnoXvDpjGGfEqFobBJWd2tC0Lyg5DqXqeQ9MK%2FEZEESfhL80NPzIz%2Bi2nkIRLjlB3MeCUxicUcNZregbm1PpldMEMhsLeUVMuiTdFedzI31CNzBLPSz37%2BmM2fcCPOV5iHc8kRUB08Nx4ectqqWWH0WK%2FrIiMtEt%2BCC5DsHVVp7VAXS%2BOFR%2FFLestl00%2BWt%2FVmiMMKeltcGOqUBQ65JldQjDfec2lsgoOmDxuMMftZY8H%2FwzdW%2B0E1HdBrwCUQNhLwk%2FhAw5ts0vAOBxR6LPbFI2v94%2Fd0PhqRY3eKt24LUSxXmsdW33zeVqydEiMOgOtsD994ZyMaaz5YlCGVsYnq5UcMJ9da7w8emjCK0GsIYjz8gL%2FmfWmr%2FBGQsaPq%2BcuRdyITqjDI7D43wQp1gTQuxp6LFrGe6w8bQqeLwIsdO&X-Amz-Signature=cf3eca7a9a757d7ec6ab9ae0b68e3ca47a09ef85dc25dd02ee752b049af7a8b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







