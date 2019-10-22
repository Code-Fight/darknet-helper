import os,shutil

path = "I:/cv_datasets/ILSVRC2012_img_train/"

file_paht = "I:/cv_datasets/train_label.txt"

with open(file_paht,"r+") as r:
    all_lines = r.readlines()

print(len(all_lines))
iterindex = 0
labels =  []
last_label = ""
with open(file_paht+".done","a+") as w:

    for line in all_lines:
        iterindex +=1
        file_name = line.split(" ")[0]
        w.write(path+file_name+"\n")
        file_name = line.split(" ")[0].split("/")[0]
        if file_name != last_label:
            labels.append (file_name)
            last_label= file_name


with open(file_paht+".label.done","a+") as w:
    for l in labels:
        w.write( l + "\n")

print(iterindex)