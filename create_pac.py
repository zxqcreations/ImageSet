import os
import numpy as np

filepath='/home/test/Assigned_video/obj_inf_output/VOC2007/ImageSets/'

f_trival = open(filepath+'trainval.txt', 'a')
f_tri = open(filepath+'train.txt', 'a')
f_var = open(filepath+'val.txt', 'a')
f_test = open(filepath+'test.txt', 'a')

t_f = os.listdir(filepath+'Main/')

for i in t_f:
    print(filepath+'Main/'+i)
    if '_train' in i:
        op = f_tri
    if '_val' in i:
        op = f_var
    with open(filepath+'Main/'+i, 'r') as f:
        for li in f:
            op.write(li.split(' ')[0] + '\n')
            f_trival.write(li.split(' ')[0] + '\n')
            if np.random.rand()<0.2:
                f_test.write(li.split(' ')[0] + '\n')
            
f_trival.close()
f_tri.close()
f_var.close()
