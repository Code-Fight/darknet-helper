import  os
import random
with open("train.txt") as f:
    data = f.readlines()



test = []
train = []
for d in data:
    index =random.randrange(1,20)
    if index==1:
        test.append(d)
    else:
        train.append(d)

with open('train_d.txt','w') as f:
    f.writelines(train)

with open('test_d.txt','w') as f:
    f.writelines(test)


print(len(train),len(test))
