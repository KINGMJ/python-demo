# -*- coding: utf-8 -*

# 使用关键字参数调用函数
def diff(x, y):
    return x - y


diff(5, 2)
diff(x=5, y=2)
diff(5, y=2)
diff(y=2, x=5)

# lambda 运算符
cube = lambda x: x ** 3
print(cube(2))
