import  os,shutil,Augmentor,json

def gen():
    list_dir = os.listdir("J:\ProjectDatasets\DDW\HXD1C-20191013\img")
    print(list_dir)
    index = 0
    for file in list_dir:
        if ".txt" in file:
            with open("J:/ProjectDatasets/DDW/HXD1C-20191013/img/"+file,"r") as f:
                r = f.read()
                if len(r)> 0 and r[0]== "0":
                    file=file.replace(".txt",".jpg")
                    shutil.copyfile("J:/ProjectDatasets/DDW/HXD1C-20191013/img/"+file, "J:/ProjectDatasets/DDW/HXD1C-20191013/new_image/"+file)

def run_Augmentor():
    p = Augmentor.Pipeline("J:/ProjectDatasets/DDW/HXD1C-20191013/new_image/")
    p.rotate(probability=0.2, max_left_rotation=18, max_right_rotation=18)
    # p.sample(50)
    p.zoom(probability=0.2, min_factor=1.1, max_factor=1.4)
    # p.sample(50)
    p.random_distortion(probability=0.2, grid_height=5, grid_width=16, magnitude=8)
    p.shear(probability=0.3, max_shear_left=15, max_shear_right=15)
    p.sample(350)
    # p.process()
    pass
def get_all():
    all =os.listdir("J:/ProjectDatasets/DDW/HXD1C-20191013/new_image/output")
    for f in all:
        print("output/"+f)

def rename_image_txt():
    list_dir = os.listdir("J:\ProjectDatasets\DDW\新建文件夹/60down")
    # print(list_dir)
    index = 20000
    for file in list_dir:
        if ".txt" in file:
            os.rename("J:\ProjectDatasets\DDW\HXD1C-20191013\img/"+file,"J:\ProjectDatasets\DDW\HXD1C-20191013\img/"+str(index)+".txt")
            file = file.replace(".txt",".jpg")
            os.rename("J:\ProjectDatasets\DDW\HXD1C-20191013\img/"+file,"J:\ProjectDatasets\DDW\HXD1C-20191013\img/"+str(index)+".jpg")
            index +=1
            print("J:\ProjectDatasets\DDW\HXD1C-20191013\img/"+str(index)+".txt")

def rename_image():
    paht  = "J:\ProjectDatasets\DDW/fist-20191021\img/"
    list_dir = os.listdir(paht)
    # print(list_dir)
    index = 30000
    for file in list_dir:

        os.rename(paht+file,paht+str(index)+".jpg")
        print(paht+str(index)+".jpg")
        index +=1


def total():
    list_dir = os.listdir("J:\ProjectDatasets\DDW/fist-20191018\img/")
    # print(list_dir)
    count=0
    for file in list_dir:
        re = float(file.split("_")[2].replace(".jpg",""))
        print(re)
        if int(re)<=95:
            # shutil.copy("J:\ProjectDatasets\DDW/fist-20191018\deal/"+file,"J:\ProjectDatasets\DDW/fist-20191018\img/"+file)
            count+=1

    print(count)

def laod_joson_to_Annotation():
    paht = "J:\ProjectDatasets\DDW/fist-20191021\img/"
    json_file = "J:/ProjectDatasets/DDW/model/20191018/result.json"
    with open(json_file,"r") as f:
        json_ret  = f.readline()
    json_ret = json.loads(json_ret)

    # print(json_ret[0])
    # return
    # print(list_dir)
    iter = 0
    for file in json_ret:
        print("img/"+file["filename"])
        filename =  str(file["filename"]).replace(".jpg",".txt")
        ret =""
        for ob in file["objects"]:
            iter+=1
            ret+= str(ob["class_id"])+" "+str(ob['relative_coordinates']['center_x'])+" "+str(ob['relative_coordinates']['center_y'])\
                  +" "+str(ob['relative_coordinates']['width'])+" "+str(ob['relative_coordinates']['height'])
            ret+="\n"
        with open(paht+filename,'w+') as w:
            w.write(ret)


    print(iter)


if __name__=="__main__":
    laod_joson_to_Annotation()


