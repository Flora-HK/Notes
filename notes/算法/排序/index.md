# 排序

快速排序常数项低，速度快优先级最大，无稳定性，空间复杂度高，归并稳定性空间复杂度高，堆排空间多时间快，空间使用率低。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/a5640f5b-e3fa-4e96-893c-684bf0fa27a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCKQKGBJ%2F20261026%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261026T072817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIBaQs%2Fz%2B%2FwLKKvlJ0HJ0T%2F0HmPF1MolhtlxipKQeSkhtAiB6fJitnjIR4HGDunb40MgN9dA7rmJxngKgg22D5pHwbyqIBAjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtLEnOQpQTJQ6h6%2FzKtwDQwtyt1GiF4yvPc7Y3sY9qYs0p1RjIaGa9S80hONyuHxrPj%2B0GoqZsl4rgvJifJbDjsC41cjrqHMFtl41rpJMtJomlQ67mH2RBfFrifFqXM1uYYBFtNO6wjaNGwpWANzURV6ORKslREuIZeVpFb1fW64C3xNarQs3QDDKHrJghGxdS%2BLHOPPiRfpY2XEi5u2OqwPmspyQtqT9MumlUcjx4vPE9vIrILT3Q%2BjGzDzGvMEfDra4Wt0nVUXtt0WAKsC8Ghj4o51QWZ07PKo0A4MUxzDWgOkwLBf9N3WSaeCKDzaFhuvKCjhoNK5DUFqmswuqb069%2F7aajt9gRRKvgQoBRsWt7JQx58y9Ams5mThwPXvojoh98ncRgGiw6GiIjU29irwc88CakT5BLc1E0srDK65wMtruggY66zgvh9Ph1Bf7smFWD%2BO9tH4K568xYA6b3Ma3sZmvQzOneBHLN%2Bvv9dfz75Y%2BpciDlMQW6%2BQVD87Q9YY1o%2BSsoRgfE%2B%2Bvmg6hzjlgAzrIq0qtrcWiCSnteeBazsMhEGBdphkw3GLo4z5pN0z%2Fc5BOca1xXNCcR7o0yYpoFrufbVkh9UlYhnzxSOwVM8IhrMt8SLqePMhCDfOQITgt%2Bfsuyln8SaYw8%2Bn71gY6pgGl%2B7ksGvEgZ8JQ3WG1zEZehr5oMD%2BJcg9WS1Iqe5B8QQhQPMYQFPQcAc8UgVWC5SbYfqMcsRtkAmk52NnMeC08gHPwT9O9ARfflh3LG9TnO3mwyKQCuNcyz5JnJmyNgIJX1fbcnceBaqtGXwXlEh3cJHx4pzrGTfKy0oB8G%2Be7dx2yYpJt5xUuyHV%2FSgIYvA%2BsmXqJcmV%2FN9%2BGsuEaaNDwlMn%2BVkHy&X-Amz-Signature=bd1273ff10a79bb24d6bf9c00ca05d1402971c793cabd8bf46a4dc68ffbdbac6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







