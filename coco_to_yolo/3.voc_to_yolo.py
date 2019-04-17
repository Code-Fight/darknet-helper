'''
这个是把coco_to_voc 按类别挑选完后，转换为yolo_mark生成的格式 直接进行使用
注意修改 images 和Annotations 以及类别 【单类测试通过，多类别没有测试】
最后修改文件前缀和 文件输出路径
'''



import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

# sets=[('2017', 'train')]

classes = ["person"]
image_path = r"F:\datasets\coco\val_result\images/"
Annotations_path = r"F:\datasets\coco\val_result\Annotations/"


def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


def convert_annotation(image_id):
    in_file = open(Annotations_path+'%s.xml'%(image_id))
    if os.path.exists(image_path+'%s.txt'%(image_id)):
        raise BaseException("请检查是否已经转换过文件")


    out_file = open(image_path+'%s.txt'%(image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')






if __name__=="__main__":
    files = os.listdir(image_path)


    files_text = []
    for f in files:
        #转换
        convert_annotation(f.split('.')[0])
        # 把所有的txt文件提取出来
        if f.split('.')[1]=="jpg":
            files_text.append(r"F:\datasets\coco\val_result\images/"+f+'\n')


    #写出整个images list
    with open(r"F:\datasets\coco\val_result/"+"train.txt",'w') as f:
        f.writelines(files_text)
        print('writing done.')