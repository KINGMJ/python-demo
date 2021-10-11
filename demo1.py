# -*- coding: utf-8 -*
list = ['Mike', 123, True]

# list 长度
print(len(list))

# 取最后一个元素
print(list[-1])

# 切片操作，返回浅拷贝
list2 = list[:]

# append 操作
list.append('Jason')
print(list2)

# list 合并操作
print(list + [456])

# list 是 mutable 类型，其内容可以改变
list[1] = 456

print(list)

# 为切片赋值可以改变列表大小，甚至清空列表
list[1:3] = []
print(list)

list[:] = []
print(list)

# 嵌套数据结构
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0][1])
