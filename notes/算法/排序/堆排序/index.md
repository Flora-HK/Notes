# 堆排序

额外空间复杂度 `O(1)`，额外空间复杂度 `O(N*logN)` 

## 一、 堆：

堆在逻辑概念上是一个完全二叉树结构。

1. 完全二叉树

一般情况下，完全二叉树的存储方式之一就是将其从上到下、从左到右存储在一个数组 `heap[]`中，所 以可以将某个数组按序展开成一个完全二叉树，数组 `heap[]`元素依次按从上到下、从左到右的顺序排列组成一个完全二叉树：

对于任意一个完全二叉树中的 `i` 位置的元素有：

1. 其左孩子为 `2*i+1` 位置、右孩子为  `2*i+2` 位置、父节点为  `(i-1)/2` 位置

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/2a419b7a-fce9-8120-8ba6-0003ab9eff18/8bedd191-adf2-454e-8d63-9be93d35ab13/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STISC5TJ%2F20261002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261002T075915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvkdBwWgaMpf0m6omvf%2F07T%2F1hKuLUIbjiBZsM3NpD1gIhANX2H47LErL6Qf4hWDzDyhREGx9yvlUu0GcJKZ%2BU9jA3KogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzCz3atI2d6Qu30YAIq3ANCedavCCqFwG51cGu7d91cdIVdFXMiO14D%2F9CoSgh7h%2FPJc9wkILXvQZ9k%2B0N5Md72xHT4eXae2aPtH2yZtHeGi69RoEsdAl1KEKiw3SFBZY%2FIFJqFk39SS63iER3ED4eybycBB4Kz2obfmn5s4QO0iA9JLxY%2BnPikvn7COlYdbFgW8gqWRmqx7xpUWXWnuMbSRWV4%2BxtPJWntc50O4giI8bPEJFDqYJ9pMgkH22WNNqbokPc2G74SXit47HAR%2FRmbHbGwJTdJoJDr4GG3Iw7RJoIjLTe9rO%2FSa2LP%2FCBd477iCulqKmNtUhd8mWOnhudfwlwz80SxP45m%2F2llZvPNE4Hw0QO00hZbq7tCRweyNkqCYa2oL1rvDtrgvv9ypUdrop8H1oWmE9kVLSgDfxkc8I8LWX4P7mXpzoL%2FTF17ynvFXhYTDKQO4%2F%2B7DeIigRvKCNNaQ3AU%2FhigyOALN8vZxFixPug4x22Lt8%2BRU%2B6wTSqeESX4HO7U%2Bu%2BW%2BLyc576CVKwfpLgbKJagTuEwaO00U%2BZWBRfLYnUg2PG6mhBS7vrguAtb3qxDHntd3v1Cz9UfxjgjNHpExzkv%2BiN6z8%2FsaCbzXYqk3TgPUGZwe48FWvQlm%2F5yn3608KlyVTCE8vzVBjqkAcsjLZnPGXkEh3mKZ%2FWEn9eCbEymDWIvuHEY4mvHMSV8HhHXn0N3qkUDAikVh1jsBeHo3myUjiiMGutk4nSGzNEVn39HDaht6ZzruDXi2AudguSau2%2FRRTr3a8Mh0Y6ElSAYIW6hG6f124GQLQ72r8n8tWd2Ihy0ZY4xZDoEwTwgnX5qy5Ryb7ZKv5nAL9syViL5Hm3ui%2BnJ62rSjLVk1DBc9URU&X-Amz-Signature=a18ff3e4daa6da934dd4db577a64eff399542e7359a2976ae53f26ab41dfd3db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. 对一个完全二叉树而言，如果其存在N个节点，则其高度为 `log(N)` 



2. 堆：

堆是一种特殊的完全二叉树，分为大根堆和小根堆

大根堆： 每一棵子树的最大值就是其头结点的值

小根堆： 每一棵子树的最小值就是其头结点的值

堆的特性：

1. 在java中，有 `PriorityQueue` 优先队列可以直接生成小根堆：
1. 在加数的时候，如果数组空间不足，可以直接成倍添加空间，每次添加空间的时间复杂度较低—— `O(N * logN)/N` ，影响较小



1. 常见的手动构建堆的两种操作：
1. 从下往上构建堆：在构建大、小根堆时（ `heepinsert`过程），先将需要插入的数放在树的叶子节点处，然后将其不断与自己的父节点进行对比，根据对比的结果考虑是否进行交换，直到不需要再进行交换

```python
def  heapinsert(arr: list[int], index: int) -> None:
    '''
    上浮调整：从下往上的大根堆调整过程、从叶子节点index到顶部
    '''
    while(index > 0 and arr[index] > arr[(index - 1) // 2]):
        arr[index], arr[(index - 1) // 2] = arr[(index - 1) // 2], arr[index]
        index = (index - 1) // 2
    return
```

b.  删除大根堆中的根部元素 `heap[0]`：（从 `index`位置开始由上往下构建堆）

将数组 `heap[]` 里的末尾处元素与0位置处的元素相交换，然后将 `heepsize - 1` 导致末尾处的元素（原 `heap[0]`）处于无效位置，以达到删除该元素的效果。

在删除之后，需要将该堆重新调整为大根堆（ `heapify`操作）：从堆顶开始查看 `heap[0]`子节点，看该元素是否有比它大的子节点（选择子节点中的更大者与当前元素进行比较），如果有比它大的子节点，那么进行交换，该节点下沉。直到该节点不再有比它大的子节点或者不再存在子节点，完成调整。

```python
def heapify(arr: list[int], index: int, heapsize: int) -> None:
    '''
    下沉调整：从index处开始调整大小为heapsize的堆arr:
    '''
    left: int = index * 2 + 1 # 左孩子节点
    while(left < heapsize): # 当左孩子节点存在时
        right: int = left + 1 # 右孩子节点
        largest: int = left
        if right < heapsize and arr[right] > arr[left]:
            largest = right # 右孩子节点存在且比左孩子节点大
        '''选出左右孩子节点中的较大的一个,将其下标传给largest'''
        if arr[index] > arr[largest]:
            break
        else:
            arr[index], arr[largest] = arr[largest], arr[index]
            index = largest # 更新“当前”位置下标
            left = index * 2 + 1 # 更新左孩子节点下标
```

有小问题：若用户任意修改了大根堆中的一个值，如何将修改后的堆调整优化成新的大根堆：

如果这个 `新值 x > 旧值 y` ——证明该新值 x 有向上调整位置的可能——对该节点调用方法 `heepinsert()` 从下往上调整堆

如果这个 `新值 x < 旧值 y` ——证明该新值 x 有向下调整位置的可能——对该节点调用方法 `heapify()` 从上往下调整堆

若该新值完全是无法预测和不可知的，那么直接先后对其调用两方法 `heepinsert()` 、 `heapify()`  即可，可以保证该新堆可以被调整成大根堆

二、 堆排序及其代码实现

1. 将待排序数组先调整成一个大根堆：从 `arr[0]` 开始，一个一个将元素插进 `heap[]` 大根堆的叶子节点中，将其插入后，对其进行 `heapinsert()` 操作。
1. 在大根堆排好之后，我们就可以确定 `arr[0]` 位置上的数字就是最大值，然后将最大值 `arr[0]`与堆尾的元素 `arr[-1]`进行交换，然后让 `heapsize - 1` ，让这个已经选出来的最大值与堆切断联系，此时，最大值已经到达了正确的位置。
1. 接下来只需要再对新的大小为 `heapsize`的堆的 `arr[0]`元素执行 `heapify()`操作，会使新的排序堆变成大根堆，此时回到a步骤，循环往复进行。
1. 当堆的大小 `heapsize == 0`的时候，即可排好顺序

代码示例如下：

```python
def heapsort(arr: list[int]) -> None:
    '''
    堆排序：时间复杂度为O(N*logN), 额外空间复杂度为O(1)
    '''
    if len(arr) <= 1:
        return
    for i in range(len(arr)):
        heapinsert(arr, i)
        print(f'heapinsert: {arr}')
    print(f'[arr] : {arr}')
    heapsize: int = len(arr) - 1
    arr[0], arr[heapsize] = arr[heapsize], arr[0]
    print(f'heapsize: {heapsize}, arr: {arr}')
    while(heapsize > 1):
        heapify(arr, 0, heapsize) 
        heapsize -= 1
        arr[0], arr[heapsize] = arr[heapsize], arr[0]
        print(f'heapsize: {heapsize}, arr: {arr}')
    return 


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    heapsort(arr)
    print(arr)


E:\DSA>E:/软件2/python/python.exe e:/DSA/排序/堆与堆排序.py
heapinsert: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
heapinsert: [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
heapinsert: [3, 1, 2, 4, 5, 6, 7, 8, 9, 10]
heapinsert: [4, 3, 2, 1, 5, 6, 7, 8, 9, 10]
heapinsert: [5, 4, 2, 1, 3, 6, 7, 8, 9, 10]
heapinsert: [6, 4, 5, 1, 3, 2, 7, 8, 9, 10]
heapinsert: [7, 4, 6, 1, 3, 2, 5, 8, 9, 10]
heapinsert: [8, 7, 6, 4, 3, 2, 5, 1, 9, 10]
heapinsert: [9, 8, 6, 7, 3, 2, 5, 1, 4, 10]
heapinsert: [10, 9, 6, 7, 8, 2, 5, 1, 4, 3]
[arr] : [10, 9, 6, 7, 8, 2, 5, 1, 4, 3]
heapsize: 9, arr: [3, 9, 6, 7, 8, 2, 5, 1, 4, 10]
heapsize: 8, arr: [4, 8, 6, 7, 3, 2, 5, 1, 9, 10]
heapsize: 7, arr: [1, 7, 6, 4, 3, 2, 5, 8, 9, 10]
heapsize: 6, arr: [5, 4, 6, 1, 3, 2, 7, 8, 9, 10]
heapsize: 5, arr: [2, 4, 5, 1, 3, 6, 7, 8, 9, 10]
heapsize: 4, arr: [3, 4, 2, 1, 5, 6, 7, 8, 9, 10]
heapsize: 3, arr: [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
heapsize: 2, arr: [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
heapsize: 1, arr: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

可以对构建初始大根堆的过程进行优化，将 `heapinsert()` 的操作换成 `heapify()` 

这样可以让初始大根堆的构建操作时间复杂度降到 `O(N)` ，代码如下：

```python
def heapsort(arr: list[int]) -> None:
    '''
    堆排序
    '''
    if len(arr) <= 1:
        return
    '''
    for i in range(len(arr)):
        heapinsert(arr, i)
        print(f'heapinsert: {arr}')
    '''
    for i in range(len(arr) - 1, -1, -1):
        '''
        对一开始的构建堆操作进行优化, 换成从叶子节点逐个执行heapify()操作，
        这样可以让该构建大根堆操作的时间复杂度变成O(N)
        '''
        print(f'[i]: {i}')
        heapify(arr, i, len(arr))
        print(f'heapify: {arr}')
    print(f'[arr] : {arr}')
    heapsize: int = len(arr) - 1
    arr[0], arr[heapsize] = arr[heapsize], arr[0]
    print(f'heapsize: {heapsize}, arr: {arr}')
    while(heapsize > 1):
        heapify(arr, 0, heapsize)
        heapsize -= 1
        arr[0], arr[heapsize] = arr[heapsize], arr[0]
        print(f'heapsize: {heapsize}, arr: {arr}')
    return 


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    heapsort(arr)
    print(arr)

```

```python
E:\DSA>E:/软件2/python/python.exe e:/DSA/排序/堆与堆排序.py
[i]: 9
heapify: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[i]: 8
heapify: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[i]: 7
heapify: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[i]: 6
heapify: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[i]: 5
heapify: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[i]: 4
heapify: [1, 2, 3, 4, 10, 6, 7, 8, 9, 5]
[i]: 3
heapify: [1, 2, 3, 9, 10, 6, 7, 8, 4, 5]
[i]: 2
heapify: [1, 2, 7, 9, 10, 6, 3, 8, 4, 5]
[i]: 1
heapify: [1, 10, 7, 9, 5, 6, 3, 8, 4, 2]
[i]: 0
heapify: [10, 9, 7, 8, 5, 6, 3, 1, 4, 2]
[arr] : [10, 9, 7, 8, 5, 6, 3, 1, 4, 2]
heapsize: 9, arr: [2, 9, 7, 8, 5, 6, 3, 1, 4, 10]
heapsize: 8, arr: [2, 8, 7, 4, 5, 6, 3, 1, 9, 10]
heapsize: 7, arr: [1, 5, 7, 4, 2, 6, 3, 8, 9, 10]
heapsize: 6, arr: [3, 5, 6, 4, 2, 1, 7, 8, 9, 10]
heapsize: 5, arr: [1, 5, 3, 4, 2, 6, 7, 8, 9, 10]
heapsize: 4, arr: [2, 4, 3, 1, 5, 6, 7, 8, 9, 10]
heapsize: 3, arr: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
heapsize: 2, arr: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
heapsize: 1, arr: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

三、常见问题

1. 存在某个堆，其元素有特点：在排好小根堆之后，任何元素的index跨度不会超过某个值k（k相对于整个数组来说是比较小的），请对符合该条件的堆进行排序

实现方法：每次选择前k + 1个数，将其输入到java的优先队列建立的小根堆里（此处使用java直接提供的小根堆是因为该算法只需要用到优先队列的有序弹入弹出功能），第一次排序就可以得出0位置上是最小的数，将该数弹出，放在 `result[]` 的0位置。然后再将第 k + 2 个数压入优先队列中，并将新小根堆的最小者弹出放在 `result[1]` 以此类推，直到 k + n 超出了范围，此时直接将排序用的小根堆元素依次弹出排列在 `result[]` 后即可

该方法时间复杂度： `O(N*logk)` ，每次对k个数进行堆排序，复杂度 `O(logk)` ，总共N个数，则为 `O(N*logk)` 

注意：

1. 在java中，有 `PriorityQueue` 优先队列可以直接生成小根堆：
1. 在加数的时候，如果数组空间不足，可以直接成倍添加空间，每次添加空间的时间复杂度较低—— `O(N * logN)/N` ，影响较小

