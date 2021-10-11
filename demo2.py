# -*- coding: utf-8 -*

# 流程控制

# x = int(input("Please enter an integer:"))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# ---------------- (●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●) ------------------

# for, python 中 for 是没有索引值的
# words = ['cat', 'window', 'apple']
# for w in words:
#     print(w, len(w))

# 遍历时同时改变集合的内容，可以遍历集合的副本或创建新的集合
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# 策略1：使用复制后的集合
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# print(users)

# 策略2：使用一个新的集合
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status

# print(active_users)

# ---------------- (●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●) ------------------

# range 函数，用于遍历数字序列
# for i in range(5):
#     print(i)

# # [5,10)
# list(range(5, 10))

# # 步进为 3
# list(range(0, 10, 3))

# # 负数，步进也应该为负
# list(range(-10, -100, -30))

# # range 和 len 结合在一起，可以像其他语言一样按索引迭代。不过大多数情况下使用 enumerate() 函数更方便
# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])


# # python3 中 range 返回的是 iterable 对象， 并没有生成真正的列表
# range(10)
# # range(0,10)
# type(range(10))
# # <class 'range'>

# ---------------- (●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●) ------------------

# break、continue以及else子句
# 循环语句支持 else 子句；for 循环中，可迭代对象中的元素全部循环完毕时，或 while 循环的条件为假时，执行该子句；
# break 语句终止循环时，不执行该子句。
# 循环的 else 子句更像 try 的 else 子句： try 的 else 子句在未触发异常时执行，循环的 else 子句则在未运行 break 时执行
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

# ---------------- (●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●)(●'◡'●) ------------------

# match 语句，类似其他语言的 switch
# _ 为通配符，必定会匹配成功
# 如果不加 _ 通配符，没有分支匹配成功，则会返回一个 None


def http_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 401 | 403 | 404:
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"


print(http_error(400))
