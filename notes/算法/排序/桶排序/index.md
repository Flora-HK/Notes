# 桶排序

一般情况下都需要根据数据状况来定制 

例：

一、记数排序：

使用一个词频数组进行统计，统计“1”出现的次数，“2”出现的次数等等，到最后n位置上的数为 i 就代表有 i 个 n ，按index顺序依次输出若干个index，致使数组有序。时间复杂度为O(N)，但是当待排数组元素量很大时，实现起来很费时。（借助数组index本身的有序性实现排序）

二、桶排序

桶：一种排序时用到的队列结构容器，元素先进先出

桶排序：

1. 准备若干个桶容器，按顺序记为 0号桶，1号桶，2号桶…，n号桶
1. 针对待排序元素的个位数字，分别将元素放入对应的桶内（个位为n就放入n号桶）：然后，再依次将0-n号桶内元素依次输出到原数组中（对某一桶内元素而言，输出遵循先进先出；对各个桶之间而言，输出顺序遵循桶的序号顺序）
1. 针对上面输出后的数组元素的十位数字，分别将其让入各桶内并依次输出
1. 针对数组元素的百位数字，再分别将其放入各桶内并依次输出
1. 完成以上四步后，即可得到排好序的数组

优于记数排序，n进制就对应n个桶即可，但是也要求待排元素必须要有进制。

三、桶排序代码实现方式：

1. 先通过分析待排元素中的最大值，来确定需要进行几次出入桶。
1. 然后通过循环依次对数组进行若干次出入桶
1. 出入桶实现方法：

a. 设定两个数组 `count[]` 和 `help[]` ，针对 `arr[]` 元素的某一位数字，将某位数字 i 出现的次数依次记录在 `count[i]` 上，然后对 `count[]` 数组进行一定的操作：将0~i 位置上的值累加，并将其存在 `count[i]` 位置上，这样我们可以得到 i 位置上的值就是当前待排序数组中 `<=i` 的元素数量；

b. 我们对待排序数组 `arr[]`从右往左（可以保证让元素先进先出）依次遍历元素，其个位数字为 i ，则将 `count[i] - 1 `，得到当前数 i 完成该次入出桶后的位置，将其放在 `help[count[i] - 1]` 上；

c. 更新词频 `count[i] = count[i] - 1` 。

d. 在依次对每一个元素都进行了如上操作，保证已经遍历了 `arr[]` 之后，将 `help[]` 倒回 `arr[]` 中，进行下一位的出入桶排序

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2ZGWY2I%2F20261124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261124T120342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB03dUz0LhzBh%2Bn6tkvclWSgrNlVFquedF46OBQPp3U8AiAIuwNMItDR8PEZcHNifsVv4YnNjLMDjEQpQrZW5RmSoSqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMICjyIqj%2FjRQOe4kxKtwDiijVdnI2%2F2NQjMoPTQ4I9%2F2gVSp4UKA7YbAO0al4iZPE5QnxhuxS2erX8%2B%2BM8X8VaktwoeRj7c4AtNC1hAVVT7Eh7y3%2BbOpMKJ81TU6%2B5kw%2FqOzV92adV2YjXPR6hI%2BbS0VwfUGJSe%2FxCiB6oYZKQd0n1SqAgbaAkG%2B7zEihjSIQLwVLl9r6RUkA1zN7PmbjhiNqKsIjwjPQdI6IhzgMymQzEttHdw2HteefmcEwqlJA0bWcu6iB0KRFoH8Cs9Q6tSXbpCgICzzlb3zaa5qLI7bjjueyYOr2%2FX%2Fh7ZneaJuablzDHyqI1IrqVbHRqgF4zXb52p19uROempw%2BoqL9B%2BhR%2BgZj3cEWswfZv03Jc7vTR%2B5AmC10O%2FeB4uw5W%2BDU2JcsoINSfo12KBYyBa%2FZu1aVVXL8kdk12mX6mLE3WIJkO4WUAyvvgF%2FKUTl47IQs8y4o4J6P6NU68bYZxa0rwQUfXZqvkQWWne4kEPk32ONwo8cTziDH8S6hmbx1nnn4DLMi1lGrSvhQ20rVBzwgyHG7fcSWnBD7B7js5m6%2F8nXx7gmw4DS3%2B3XMn5KnuZbkcpiPYff974r2BALrA4LFitdQoOIBs41nQES7BSYO3R%2FL%2F4XEfvQF%2FU6sJUMwotmV2AY6pgF%2BRLv8E2M2nXSF2K7HuVkiQqwp5Xe0vj%2Byi1ziuaZ%2B9c%2F98qjXwP%2B1ggGcrunADF4IM23fVm%2FtC9hz8Ke2fhhzOfDZ%2Bv9kEFESXpfHJmz8GVUKmY5aPUUj40JBgOJblJUTgrViQHOs8%2FhQetqTdxcWD9VhmG5v%2FnRUOaFsEkLu5tFRmczNE9hsVL%2FiUXHzITxZCIiBRxQ8xzDCGmkUmT1N%2FZ8kkv47&X-Amz-Signature=10c11cb7612e94fac77d26d0e762d5312669f54a9a82e0e39a6101454fa2e2c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2ZGWY2I%2F20261124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261124T120342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB03dUz0LhzBh%2Bn6tkvclWSgrNlVFquedF46OBQPp3U8AiAIuwNMItDR8PEZcHNifsVv4YnNjLMDjEQpQrZW5RmSoSqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMICjyIqj%2FjRQOe4kxKtwDiijVdnI2%2F2NQjMoPTQ4I9%2F2gVSp4UKA7YbAO0al4iZPE5QnxhuxS2erX8%2B%2BM8X8VaktwoeRj7c4AtNC1hAVVT7Eh7y3%2BbOpMKJ81TU6%2B5kw%2FqOzV92adV2YjXPR6hI%2BbS0VwfUGJSe%2FxCiB6oYZKQd0n1SqAgbaAkG%2B7zEihjSIQLwVLl9r6RUkA1zN7PmbjhiNqKsIjwjPQdI6IhzgMymQzEttHdw2HteefmcEwqlJA0bWcu6iB0KRFoH8Cs9Q6tSXbpCgICzzlb3zaa5qLI7bjjueyYOr2%2FX%2Fh7ZneaJuablzDHyqI1IrqVbHRqgF4zXb52p19uROempw%2BoqL9B%2BhR%2BgZj3cEWswfZv03Jc7vTR%2B5AmC10O%2FeB4uw5W%2BDU2JcsoINSfo12KBYyBa%2FZu1aVVXL8kdk12mX6mLE3WIJkO4WUAyvvgF%2FKUTl47IQs8y4o4J6P6NU68bYZxa0rwQUfXZqvkQWWne4kEPk32ONwo8cTziDH8S6hmbx1nnn4DLMi1lGrSvhQ20rVBzwgyHG7fcSWnBD7B7js5m6%2F8nXx7gmw4DS3%2B3XMn5KnuZbkcpiPYff974r2BALrA4LFitdQoOIBs41nQES7BSYO3R%2FL%2F4XEfvQF%2FU6sJUMwotmV2AY6pgF%2BRLv8E2M2nXSF2K7HuVkiQqwp5Xe0vj%2Byi1ziuaZ%2B9c%2F98qjXwP%2B1ggGcrunADF4IM23fVm%2FtC9hz8Ke2fhhzOfDZ%2Bv9kEFESXpfHJmz8GVUKmY5aPUUj40JBgOJblJUTgrViQHOs8%2FhQetqTdxcWD9VhmG5v%2FnRUOaFsEkLu5tFRmczNE9hsVL%2FiUXHzITxZCIiBRxQ8xzDCGmkUmT1N%2FZ8kkv47&X-Amz-Signature=d43c79b0582a6eaa4a4aa193fb38b8e0bfb3d6592086be341fb1a006bd12f0b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



