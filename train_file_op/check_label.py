'''
检查标记中是否有超过标定的label
比如3个类别  检查是否有大于2的 并打印出来
'''

import os

with open("J:\ProjectDatasets\DDW\sword_fist_zhanli_20191101\data/train.txt","r") as f:
    data = f.readlines()

for  d in data:

    if d !="":
        # print(d.split(" ")[0])
        d = d.replace("\n","").replace(".jpg",".txt")
        with open(d,"r") as df:
            df_data = df.readlines()
        for dfd in df_data:
            if len(dfd) >0:
                # print(dfd.split(" ")[0])

                if int(dfd.split(" ")[0])>2:
                    print(d)