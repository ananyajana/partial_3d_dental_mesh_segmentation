#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 14:14:36 2022

@author: aj611
"""

from vedo import *
import vedo
import os
from glob import glob
#dataurl = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/data/3dteethseg_all_vtps_combined_16k_15class_meshes_cropped/'
#dataurl = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/data/all_vtps_combined_flipped_16k_8_class/'
dataurl='/research/cbim/medical/aj611/experiments/biomed_2022/mesh/data/3dteethseg_all_vtps_combined_flipped_16k_8class_meshes_cropped/'
#output_path = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/data/single_vtp_16k_8_class_half_jaw/'
#output_path = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/data/all_vtps_combined_flipped_16k_8_class_half_jaw/'
output_path = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/data/3dteethseg_all_vtps_combined_flipped_16k_8class_meshes_cropped_half_jaw/'

os.makedirs(output_path, exist_ok=True)





all_files = glob(dataurl + '*.vtp')
'''
#print(all_files)
#raise ValueError("Exit!")

label_color_map = {'0':[254, 254, 254], '1': [252, 128, 3], '2': [252, 235, 3], '3': [198, 252, 3], '4': [3, 252, 235]  , '5': [3, 173, 252] , '6': [177, 3, 252] ,\
                   '7': [191, 8, 8]}

# this sample is from the test_list_3.csv file,
f1 = os.path.join(dataurl, 'Sample_024_d.vtp')
#f1 = os.path.join(dataurl, 'Sample_024_d_flip.vtp')  
s = Mesh(f1) 

print(s.NCells())
#print('labels len :', len(s.celldata['labels']))
print('labels len :', len(s.celldata['labels']))
labels_arr = s.celldata['labels']
print(labels_arr)

colorlist = []    
for i in range(len(labels_arr)):
    cur_label = int(labels_arr[i])
    colorlist.append(label_color_map["{:d}".format(cur_label)])
s.cellIndividualColors(colorlist)
#s.cellIndividualColors


 

#--------------------- current one
#s_mod = s.crop(right=0.78).crop(top=0.52) # this is cur in such a way that sample_01_d.vtp has a single molar after this operation
s.crop(right=0.48) # this is cur in such a way that sample_01_d.vtp has a single molar after this operation
#print('labels len for s_mod:', len(s_mod.celldata['labels']))
s.show()
#s_mod.show()
    
    
'''
for i in range(len(all_files)):
    f1 = all_files[i]

    s = Mesh(f1) 

    print(s.NCells())

    #s_mod = s.crop(right=0.78).crop(top=0.52) # this is cur in such a way that sample_01_d.vtp has a single molar after this operation
    #s_mod = s.crop(right=0.78) # this is cur in such a way that sample_01_d.vtp has a single molar after this operation
    s_mod = s.crop(right=0.48)
    #print('labels len for s_mod:', len(s_mod.celldata['labels']))
    #s.show()
    #s_mod.show()
    #raise ValueError("Exit!")


    f_name = f1.split('/')[-1]
    print('f_name', f_name)
    #raise ValueError("Exit!")
    write(s_mod, os.path.join(output_path, f_name))


