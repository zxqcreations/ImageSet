import os

file_path = '/home/test/Assigned_video/obj_inf_output/VOC2007/Annotations/'

l_s = os.listdir(file_path)

for i in l_s:
    with open(file_path+i, 'r') as f:
        t = f.read()
        t = t.replace('<xmin>0</xmin>','<xmin>1</xmin>').replace('<ymin>0</ymin>','<ymin>1</ymin>')
             
    with open(file_path+i, 'w') as f:
        f.write(t)
