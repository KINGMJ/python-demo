# -*- coding: utf-8 -*

# 标准库

# os
import os
# 获取当前目录
print(os.getcwd())

# 获取用户目录 ~
user_path = os.path.expanduser('~')
# 切换目录
os.chdir(user_path + '/MyCode/test')
# 运行系统命令
os.system('mkdir today')

# shutil 高阶文件操作
