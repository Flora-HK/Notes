# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNJAXN5O%2F20261027%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261027T072237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJGMEQCIAdIg7aVvQAFmB9fFQmFY72Z01yD%2B237AOG3t240uQxzAiAcJtefci0xRmAnmceOFEBUp3ue6%2FnLJ4cIgU%2FOe5kAPCqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMDYKgx8LoGwbkedhKtwD6trxOyyzusQVxfg60UdCJ1ogB6ACLmgYzybGoW7TcfZdQvZf%2BycFwHGlJA3WPyVWN3z%2F6fnOkEzPw8JXEQvBE56sjt39DzUH9t%2B2nKOy%2B6ZtpLcXdWivGbCRR6ChALpeQtDQJo6X%2FQBuXUGZqIiA2F%2FqRvu35TextQMG78Lrb6a1Aj%2Fom7%2ByiFfl9GcT0Uf2L%2FKSXABpOfnCi%2F8y7nIgz5eQypG6k%2FS220lZ516SNYkcnl1KaLO5DDtsclEh1b76MGTq3IJxxKuJuplGMoVJlkB36qtzFg9tu3Zl0JbjP56UyHHxvXe39m1qPlxjbWI40dykiOuQxvEflSb%2FENRxS2iU1jUkUOGQU0yMo7mlPLJYQFHYqkE8WUPJ2dglkc19jA6JESFclRXjhV9A5cdLKjPsRYy5AegzFXkwXFmmmNJItXBw4QBvKQdj1VtTiUBS%2FE5hrnxOioR1mzk9k2s479eRoYCfAtIIgBJAyN5VifhG6xzSgde0njEQxvLIxH%2FQGRwreGlIUvLdr5ofr1tef92P5wjdNZTIumgN0q45Oo0N%2FLgJC8SnOcXB%2BLwyytl81vElbECWgDqcAYcBT5xpMx5Zjh4LGdUNWytXcXgCdqq2BDey6c1Akm37eskwiJGB1wY6pgGVjWm%2FyR5Y3KZX4LsNXYCptHCa%2F2%2BBTLGAiITo2qeZdC4RBwOgfJsqeX%2FU8%2BbyBuFCJU6hAzRYeGN1PsBq1M0AgJvNeDef69Ul8T30nNvIJ%2FIZb6J5C0AQLAEzpCV8uorgUALdfjGPTtyKK4fUML16FBtrtknQl9hLMdp1tUZdR3UT6fk1OY9z58TjRe82DVOLpOYJ5tWmqEyGmh6i2anPVxVXajrV&X-Amz-Signature=fcf22e0bc90bb28935ef1d4880bd3c0a0635ee0aa59fe5b264b2a5f50ee35026&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







