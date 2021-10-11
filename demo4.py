# -*- coding: utf-8 -*

# 遍历的技巧

# items() 可以取出 key 和 value
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# enumerate() 可以取出 index 和 value
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 同时循环多个序列时，zip() 函数可以将其内的元素一一匹配
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

# 排序加去重
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
