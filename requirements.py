#在项目里生成requirements.txt
import os, sys
# 找到当前目录
project_root = os.path.dirname(os.path.realpath(__file__))
print(project_root)

# 找到解释器，虚拟环境目录
python_root = sys.exec_prefix
print(python_root)

# 拼接生成requirements命令
command = python_root + '\Scripts\pip freeze > ' + project_root + '\\requirements.txt'
print(command)

# 执行命令。
os.system(command)