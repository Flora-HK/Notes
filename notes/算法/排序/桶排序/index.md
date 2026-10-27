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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQBFPETV%2F20261027%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261027T072238Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJHMEUCIQDr0aw1EfvnAD3U%2BCweco7tRfqVPIKP5nbMR7%2BYdMNuXQIgANOgrM0LJHG5LpK5XbLcRlCYVflHnsQ%2F9yI2Ax%2FF1uQqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFCj7gnjs8D0dqNaVircAxlFSDBIttPiZruEFf4LBaFZ5lcrdJ77YkZO%2FOenldfM%2Bd%2By%2BbtyHo4oJQH36Mt5nFZDVqae7islPRN7HX%2BZ5f0zh1SODSJ6crGNPSGosz1hwbAZ6y5UGcS1F52n5c7BewAxpchCTIvQzIumpKcCfbaklQXErQnunbbFwzgUeEFkUL4wh7NUNG1CZTC2vuPjwBJuMGDc7%2FbUeKQ5oCxzteS6Hr9hdUVuKwC04wBBdYZbz7UEKtbdwOjnum19xrf0uEh9yVTtD8TZy9HHQNhjo4sZsqUSkTSY1fy%2FSqvrE%2B7hqLqF3kePAeUXdX%2BHslZtu%2F6X1fk%2FOca5qcH6wId8Ng80%2BVrf%2FZU7LZBu33ObQTiZN%2BwQptSCXmicteus5ProtBJ%2B2XVYLFNcZkSmwYeJNRm3mkcOnu8Bds5fVUBYlw31dWTtcm0666DNwLbv%2FYF8FvPKX2Fj6Bw8ojsVusnP1moyHZpAhAX5j7q7ZYFliVy4O5gxSqjOw1Tv0wPYYyjhm8gpVmod3OZeY%2FaWXlgCRJoaqyxpomR6IT0%2B3Woo5Q%2BEknyqm7dPkIkzhloPF7uZ7wF4h6ajIH2HjVtUg6DPBH7GhFxnu4xzyL1%2Fslsvk3ExDtetcJAp8JPrJaIFMIaRgdcGOqUBmaLm0gbBHk5vwCABld7gn5OpixISkISrXQt1JogYiPyKy4Dg1lAWgCdhm88LTGygT03AYM4ZuNv5FmJjBVEGT8bk2lNZfPJPQXiZuOSNnwlXmflw8AiHrBcixEpJGE%2BfWydCsp1V0SysIDQNu%2Ff8NisbHSXQ4GE74eU%2BbzwCJwpUDoG2jsAma%2Fe5MdJHH2cjSS7erD6yZRYW6KrPYUt%2F3M%2Bf0f2A&X-Amz-Signature=c9049e8fb7b9c2aa8a799fa0f290a85fcf50b2927322fc635509ccd63e1b26eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQBFPETV%2F20261027%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261027T072238Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJHMEUCIQDr0aw1EfvnAD3U%2BCweco7tRfqVPIKP5nbMR7%2BYdMNuXQIgANOgrM0LJHG5LpK5XbLcRlCYVflHnsQ%2F9yI2Ax%2FF1uQqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFCj7gnjs8D0dqNaVircAxlFSDBIttPiZruEFf4LBaFZ5lcrdJ77YkZO%2FOenldfM%2Bd%2By%2BbtyHo4oJQH36Mt5nFZDVqae7islPRN7HX%2BZ5f0zh1SODSJ6crGNPSGosz1hwbAZ6y5UGcS1F52n5c7BewAxpchCTIvQzIumpKcCfbaklQXErQnunbbFwzgUeEFkUL4wh7NUNG1CZTC2vuPjwBJuMGDc7%2FbUeKQ5oCxzteS6Hr9hdUVuKwC04wBBdYZbz7UEKtbdwOjnum19xrf0uEh9yVTtD8TZy9HHQNhjo4sZsqUSkTSY1fy%2FSqvrE%2B7hqLqF3kePAeUXdX%2BHslZtu%2F6X1fk%2FOca5qcH6wId8Ng80%2BVrf%2FZU7LZBu33ObQTiZN%2BwQptSCXmicteus5ProtBJ%2B2XVYLFNcZkSmwYeJNRm3mkcOnu8Bds5fVUBYlw31dWTtcm0666DNwLbv%2FYF8FvPKX2Fj6Bw8ojsVusnP1moyHZpAhAX5j7q7ZYFliVy4O5gxSqjOw1Tv0wPYYyjhm8gpVmod3OZeY%2FaWXlgCRJoaqyxpomR6IT0%2B3Woo5Q%2BEknyqm7dPkIkzhloPF7uZ7wF4h6ajIH2HjVtUg6DPBH7GhFxnu4xzyL1%2Fslsvk3ExDtetcJAp8JPrJaIFMIaRgdcGOqUBmaLm0gbBHk5vwCABld7gn5OpixISkISrXQt1JogYiPyKy4Dg1lAWgCdhm88LTGygT03AYM4ZuNv5FmJjBVEGT8bk2lNZfPJPQXiZuOSNnwlXmflw8AiHrBcixEpJGE%2BfWydCsp1V0SysIDQNu%2Ff8NisbHSXQ4GE74eU%2BbzwCJwpUDoG2jsAma%2Fe5MdJHH2cjSS7erD6yZRYW6KrPYUt%2F3M%2Bf0f2A&X-Amz-Signature=f3c0b8d2c0912af65d5f60cb6cf2d790364624a0c93afc4c02cfd3a7c3ae005c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



