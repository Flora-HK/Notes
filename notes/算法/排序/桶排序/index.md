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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/79b2a317-63ab-42bd-9194-d90f4e5fccd4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QQCNHIN%2F20261031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261031T080147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJIMEYCIQDs2M4gnvXg3dgRcAR9Wu4ZS8beATIM8BVi6gCUnOJB2QIhALUKQ2uFeaeYQtxOLt4H8mZAx5jiM5CNpKQOS1xvIvYyKv8DCEgQABoMNjM3NDIzMTgzODA1IgzNcPx2qYLheYzK6hgq3AP8BYyXtj%2FMlajlJSFism4mC2Wkp1OudgKoWazLCI%2BZEJCHKwnUuiJsZKvHv4y%2BN%2F2FaBPTjZZZs7iLL7%2F%2FXmqUxk%2Fgoocc2xFIe5Kww8zwQW8yqLYr5t8r43h0tNvAx8YUtF78ApMJdo8%2BHfPpRVWJXtqeRFIjAIwqVQMRDT2KQo745pM8qC0S0TjzBsZWQkI2IK7%2BdcqzSfjFpL0ddapJp42b7rWrxURgoaohIwGXiub2fSFQ192zvFPQux0HI7jDEJKifvrsJ2JthBYD3nqtTuBNvwyfhDjskyTxv68Wk8hTrdPbB5MvP0gfkKIcUmmTMDcMx%2B7rZif44SBRBZHgggFOsK18OKjRLzGKBAapFoXWSsC%2BoFN32479Hqgz4KZzwO31ix%2BPdgymzmO4U9jlF2T0y375UZw4Ok7w%2BkEykFR5airxLrtUySPwwxYXFhNR6maFE30I%2FifNrPU9uNyVcljCiMOKDuKiwA0%2BAJZcyXzOoOe%2Bqcgrztq4iKcWMJglgM20M%2BdghWq8Nq0aWw0K2WyxX0kfCML2r4zkWd42aTUmncM9wwH18Uuj22TIn2%2F6CuD0kyTZWtk%2BY2E3FtxfyfJFsY4mMJz%2FXKmk7TPXrkL3mfbOpR3CNk%2BE5TDBnpbXBjqkATb2TzSwHyhi1myfVR11PUxl9tAfAYG3hFOtJQVnAdlD7BzJLdZxLw1k8KMeQt%2BCFzSFIdtRMi4Rw%2BKY1%2BUe5wxjnmLDZyfbO3FZZlxvyP0ofphf4I6zcQCFmAAr3%2Frk9Lpdv%2Fs22XBnxFp4ubFNrXd7Kq0lbKiclNtqpQ9hXnNW6r8RrXXlL5gEGLD%2FFjIiU7C83pv%2B30Sj%2BelJbUq453w2wu%2Bh&X-Amz-Signature=d870ed209670b8860ad830e33c6cb4c3c91ce97a9c8c84825974e2add2fe20a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/9acfca21-6bff-444a-8975-bc5bd6bab6dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QQCNHIN%2F20261031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261031T080147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJIMEYCIQDs2M4gnvXg3dgRcAR9Wu4ZS8beATIM8BVi6gCUnOJB2QIhALUKQ2uFeaeYQtxOLt4H8mZAx5jiM5CNpKQOS1xvIvYyKv8DCEgQABoMNjM3NDIzMTgzODA1IgzNcPx2qYLheYzK6hgq3AP8BYyXtj%2FMlajlJSFism4mC2Wkp1OudgKoWazLCI%2BZEJCHKwnUuiJsZKvHv4y%2BN%2F2FaBPTjZZZs7iLL7%2F%2FXmqUxk%2Fgoocc2xFIe5Kww8zwQW8yqLYr5t8r43h0tNvAx8YUtF78ApMJdo8%2BHfPpRVWJXtqeRFIjAIwqVQMRDT2KQo745pM8qC0S0TjzBsZWQkI2IK7%2BdcqzSfjFpL0ddapJp42b7rWrxURgoaohIwGXiub2fSFQ192zvFPQux0HI7jDEJKifvrsJ2JthBYD3nqtTuBNvwyfhDjskyTxv68Wk8hTrdPbB5MvP0gfkKIcUmmTMDcMx%2B7rZif44SBRBZHgggFOsK18OKjRLzGKBAapFoXWSsC%2BoFN32479Hqgz4KZzwO31ix%2BPdgymzmO4U9jlF2T0y375UZw4Ok7w%2BkEykFR5airxLrtUySPwwxYXFhNR6maFE30I%2FifNrPU9uNyVcljCiMOKDuKiwA0%2BAJZcyXzOoOe%2Bqcgrztq4iKcWMJglgM20M%2BdghWq8Nq0aWw0K2WyxX0kfCML2r4zkWd42aTUmncM9wwH18Uuj22TIn2%2F6CuD0kyTZWtk%2BY2E3FtxfyfJFsY4mMJz%2FXKmk7TPXrkL3mfbOpR3CNk%2BE5TDBnpbXBjqkATb2TzSwHyhi1myfVR11PUxl9tAfAYG3hFOtJQVnAdlD7BzJLdZxLw1k8KMeQt%2BCFzSFIdtRMi4Rw%2BKY1%2BUe5wxjnmLDZyfbO3FZZlxvyP0ofphf4I6zcQCFmAAr3%2Frk9Lpdv%2Fs22XBnxFp4ubFNrXd7Kq0lbKiclNtqpQ9hXnNW6r8RrXXlL5gEGLD%2FFjIiU7C83pv%2B30Sj%2BelJbUq453w2wu%2Bh&X-Amz-Signature=69f23544efe281a45eb3192988ee0c975846d4435b5e73a378b65e99948e49e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



