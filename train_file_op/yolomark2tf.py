import  os
from PIL import Image


with open('train.txt', 'r') as train_list:
    for lst in train_list.readlines():
        lst = lst.strip()
        jpg = lst  # image path
        txt = lst.replace('.jpg', '.txt')  # yolo label txt path

        obj = ''

        img = Image.open(jpg)


        img_w,img_h = img.size[0],img.size[1]
        with open(txt, 'r') as f:
            for line in f.readlines():
                yolo_datas = line.strip().split(' ')
                label = int(float(yolo_datas[0].strip()))
                center_x = round(float(str(yolo_datas[1]).strip()) * img_w)
                center_y = round(float(str(yolo_datas[2]).strip()) * img_h)
                bbox_width = round(float(str(yolo_datas[3]).strip()) * img_w)
                bbox_height = round(float(str(yolo_datas[4]).strip()) * img_h)

                xmin = (int(center_x - bbox_width / 2))
                ymin = (int(center_y - bbox_height / 2))
                xmax = (int(center_x + bbox_width / 2))
                ymax = (int(center_y + bbox_height / 2))

                if xmin <=0:
                    print("xmin")

                if ymin<=0:
                    print("ymin")

                if xmax>img_w:
                    print("img_w")
                if ymax > img_h:
                    print("img_h")


                continue

                # obj += xml_obj.format(labels[label], xmin, ymin, xmax, ymax)
        with open("train_output.txt", 'a') as w:
            w.write(str(lst)+" "+str(xmin)+","+str(ymin)+","+str(xmax)+","+str(ymax)+","+str(label)+"\r")
