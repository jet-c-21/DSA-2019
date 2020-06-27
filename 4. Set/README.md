###### tags: `GitHub - DSA2019`
# What is Set ?
> <font size = 2 >Original Author : [aaron1aaron2](https://github.com/aaron1aaron2) -《[Set](https://github.com/aaron1aaron2/my-learning-note/blob/master/week4/readme.md#set)》</font>

<br>

## 維基百科定義
在數學定義上，它是集合論的研究物件，指具有某種特定性質的事物的母體，「一堆東西」集合裡的事物東西叫作元素。數字 2、4和 6 在單獨考慮時是不同的對象，但是當將它們放一起時，會形成的大小為3的單個集合- {2,4,6}。

## 特性
* Set集合裡沒有重複元素
* Set集合是無序集合

## 基本操作
* 插入
* 刪除
* Set 是否為空
* Set 是否包含某個元素
* Set 元素個數
## 在 python 裡的基本操作
```python=
a = {1,2,3}
b = {2,5,6}

a&b # 交集:{2}

a|b # 聯集:{1, 2, 3, 5, 6}

a-b # 差集:{1, 3}

2 in a # True
2 not in a # False
```
## 其他符號
|python 符號|意思|
|:-:|:-|
|---|差集|
|&|交集|
|I|聯集|
|!=|不等於|
|==|等於|
|in|屬於|
|not in|不屬於|
