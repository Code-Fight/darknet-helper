import os,shutil


file_paht = "I:/cv_datasets/train_label.txt"

with open(file_paht,"r+") as r:
    all_lines = r.readlines()

print(len(all_lines))
iterindex = 0
labels = set()
for line in all_lines:
    iterindex += 1
    file_name = line.split(" ")[0].split("/")[0]
    labels.add(file_name)

with open(file_paht+".label.done","a+") as w:
    for l in labels:
        w.write( l + "\n")






print(iterindex)