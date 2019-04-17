'''
这个主要来检查 coco_to_voc 按照类别提取完后，是不是正确
主要要修改路径 一个是image 一个是 annotations
最后修改 输出保存的路径和数量 即可
'''

from __future__ import division
import os
from PIL import Image
import xml.dom.minidom
import numpy as np
import cv2
ImgPath = 'F:/datasets/coco/resultimages/'
AnnoPath = 'F:/datasets/coco/resultAnnotations/'

imagelist = os.listdir(ImgPath)
a = 0
for image in imagelist:
    image_pre, ext = os.path.splitext(image)
    imgfile = ImgPath + image
    xmlfile = AnnoPath + image_pre + '.xml'

    DomTree = xml.dom.minidom.parse(xmlfile)
    annotation = DomTree.documentElement

    filenamelist = annotation.getElementsByTagName('filename')  # [<DOM Element: filename at 0x381f788>]
    filename = filenamelist[0].childNodes[0].data
    objectlist = annotation.getElementsByTagName('object')

    i = 1
    for objects in objectlist:
        # print objects

        namelist = objects.getElementsByTagName('name')
        # print 'namelist:',namelist
        objectname = namelist[0].childNodes[0].data

    bndbox = objects.getElementsByTagName('bndbox')
    cropboxes = []

    for box in bndbox:
        try:
            x1_list = box.getElementsByTagName('xmin')
            x1 = int(x1_list[0].childNodes[0].data)
            y1_list = box.getElementsByTagName('ymin')
            y1 = int(y1_list[0].childNodes[0].data)
            x2_list = box.getElementsByTagName('xmax')
            x2 = int(x2_list[0].childNodes[0].data)
            y2_list = box.getElementsByTagName('ymax')
            y2 = int(y2_list[0].childNodes[0].data)
            w = x2 - x1
            h = y2 - y1






        except BaseException as e:
            print(e)
    img = Image.open(imgfile)
    width, height = img.size

    image = cv2.imread(imgfile)
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    # cv2.cv.ShowImage('rectangle', image)
    cv2.imwrite('D:/'+str(a)+'.jpg', image)
    a += 1
    if a > 9:
        break