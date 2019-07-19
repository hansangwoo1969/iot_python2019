import sys


a = sys.path
with open("sys_path.txt", 'w', encoding='UTF-8') as f:
    for i in sys.path:
        f.write(i)
        f.write('\n')
