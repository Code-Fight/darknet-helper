# coding=utf-8

'''
修改指定path下的文件名称,并可以带参数打印
1.修改path
2.修改file_hz 文件后缀
3.修改打印参数 file_path_params 点缀打印的数据用
'''

import os

path = r'D:\out\1'
file_hz='.jpg'
file_path_params='data/img/'
count = 1
for file in os.listdir(path):
    os.rename(os.path.join(path, file), os.path.join(path, str(count) + file_hz))
    print(file_path_params + str(count) + file_hz)
    count += 1
