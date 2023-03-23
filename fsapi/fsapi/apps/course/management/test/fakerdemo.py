#!/usr/bin/env python

# 首行以后的代码必须要符合python的语法
"""
针对通用代码的运行，可以直接使用系统内置的全局环境的python解释器，也可以使用虚拟环境的解析器
如果这个代码需要调用对应的第三方模块，那么就要写上安装该模块的python解释器
"""
import os, sys
from faker import Faker

faker = Faker(["zh_CN"])
user = faker.unique.name()
print(f"hello，{user}")

# python获取终端参数
try:
    dir = sys.argv[1]
except Exception as e:
    dir = "2023"

# python直接执行shell命令
ret = os.popen(f"mkdir {dir} && cd {dir} && echo 'hello {user}' > test.txt")
print(ret.read())
