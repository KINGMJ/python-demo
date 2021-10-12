# -*- coding: utf-8 -*

# tuple，元组是 immutable 的
t = 123, 'hello'
print(t)
print(t[0])

u = t, (1, 2, 3, 4, 5)
print(u)

r, g, b = (255, 255, 0)
print(r, g, b)

# ---------------- (●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●) ------------------


# Sets 集合

# 集合是由不重复元素组成的无序容器，空集合使用 set 来创建，{} 创建的是空字典
basket = {'apple', 'orange', 'apple', 'orange'}
print(basket)
# {'apple', 'orange'}

a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)
# {'b', 'r', 'd', 'a', 'c'}
# {'l', 'z', 'm', 'a', 'c'}

# 集合的差集、交集等操作
# letters in a but not in b
print(a - b)
# letters in a or b or both
print(a | b)
# letters in both a and b
print(a & b)
# letters in a or b but not both
print(a ^ b)

# 字典 Dictionaries
tel = {'jack': 4098, 'sape': 4139}
tel['amy'] = 2191
print(tel)
# {'jack': 4098, 'sape': 4139, 'mary': 2191}
del(tel['sape'])
print(tel)
print(list(tel))
print(sorted(tel))


# 使用 dict() 创建字典
dict1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict1)

# 关键字是比较简单的字符串时，直接用关键字参数指定键值对更便捷：
dict2 = dict(sape=4139, guido=4127, jack=4098)
print(dict1)
