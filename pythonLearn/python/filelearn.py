#文件操作

# 查找指定文件格式的文件
import os

def find_file(work_dir,extension='jpg'):
    lst = []
    for filename in os.listdir(work_dir):
        print(filename)
        splits = os.path.splitext(filename)
        print('splits:',splits)
        ext = splits[1] # 拿到扩展名
        if ext == '.'+extension:
            lst.append(filename)
    print('lst:', lst)
    return lst

if __name__ == "__main__":

    find_file('.','md') # 返回所有目录下的md文件