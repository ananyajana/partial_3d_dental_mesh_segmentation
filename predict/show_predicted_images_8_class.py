#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 14:14:36 2022

@author: aj611
"""

from vedo import *
import os
#dataurl = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/data/all_vtps_combined_16k_meshes/'
#dataurl='/research/cbim/medical/aj611/experiments/biomed_2022/mesh/data/3dteethseg_all_vtps_combined_flipped_16k_8class_meshes_cropped/'
#dataurl='/research/cbim/medical/aj611/experiments/biomed_2022/mesh/data/3dteethseg_all_vtps_combined_flipped_16k_8class_meshes_cropped_molar/'
#dataurl='/research/cbim/medical/aj611/experiments/biomed_2022/mesh/data/3dteethseg_all_vtps_combined_flipped_16k_8class_meshes_cropped_half_jaw/'
#dataurl='/research/cbim/medical/aj611/experiments/biomed_2022/mesh/data/3dteethseg_all_vtps_combined_flipped_16k_8class_meshes_cropped_front/'
#dataurl='/research/cbim/medical/aj611/experiments/biomed_2022/mesh/data/3dteethseg_all_vtps_combined_flipped_16k_8class_meshes_cropped_four_teeth/'
#dataurl='/research/cbim/medical/aj611/experiments/biomed_2022/mesh/data/3dteethseg_all_vtps_combined_flipped_16k_8class_meshes_cropped_three_teeth/'
#dataurl='/research/cbim/medical/aj611/experiments/biomed_2022/mesh/data/3dteethseg_all_vtps_combined_flipped_16k_8class_meshes_cropped_ten_teeth/'
#dataurl='/research/cbim/medical/aj611/experiments/biomed_2022/mesh/data/3dteethseg_all_vtps_combined_flipped_16k_8class_meshes_cropped_eight_teeth/'
#dataurl = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/pred_162/outputs/'
#dataurl = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/pred_162/outputs_single_tooth_molar/'
#dataurl = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/pred_162/outputs_single_tooth_half_jaw/'
#dataurl = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/pred_162/outputs_single_tooth_front/'
#dataurl = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/pred_162/outputs_single_tooth_four_teeth/'
#dataurl = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/pred_162/outputs_single_tooth_three_teeth/'
#dataurl = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/pred_162/outputs_single_tooth_ten_teeth/'
#dataurl = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/pred_162/outputs_single_tooth_eight_teeth/'
#dataurl = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/pred_162/outputs_gco2/'
#dataurl = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/pred_162/outputs_gco2_front/'
#dataurl = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/pred_162/outputs_gco2_half_jaw/'
#dataurl = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/pred_162/outputs_gco2_molar/'
#dataurl = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/pred_162/outputs_gco2_four_teeth/'
#dataurl = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/pred_162/outputs_gco2_three_teeth/'
#dataurl = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/pred_162/outputs_gco2_ten_teeth/'
dataurl = '/research/cbim/medical/aj611/experiments/biomed_2022/mesh/pred_162/outputs_gco2_eight_teeth/'

#s = Mesh(os.path.join(dataurl+'Sample_024_d.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_024_d_predicted_dgcnn.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_024_d_predicted_pointnet.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_024_d_predicted_pointnet2.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_024_d_predicted_pointmlp.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_024_d_predicted_pct.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_024_d_predicted_gac.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_024_d_predicted_tsgcn.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_024_d_predicted_mmnet.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_024_d_predicted_meshsegnet.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_024_d_predicted_mbesegnet.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_021_d_predicted_gac.vtp'))


#s = Mesh(os.path.join(dataurl+'Sample_033_d.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_033_d_predicted_pointnet.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_033_d_predicted_pointnet2.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_033_d_predicted_dgcnn.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_04_d_predicted_mmnet.vtp'))

#s = Mesh(os.path.join(dataurl+'Sample_120_d_predicted_pct.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_0542_d_predicted_meshsegnet.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_0542_d_predicted_pct.vtp'))

#s = Mesh(os.path.join(dataurl+'Sample_042_d.vtp'))

#s = Mesh(os.path.join(dataurl+'Sample_042_d_predicted_pct.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_042_d_predicted_pointnet.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_042_d_predicted_pointnet2.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_042_d_predicted_dgcnn.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_042_d_predicted_meshsegnet.vtp'))
s = Mesh(os.path.join(dataurl+'Sample_042_d_predicted_refined_meshsegnet.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_042_d_predicted_pct.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_042_d_predicted_pointmlp.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_042_d_predicted_mmnet.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_042_d_predicted_mbesegnet.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_042_d_predicted_tsgcn.vtp'))
#s = Mesh(os.path.join(dataurl+'Sample_042_d_predicted_gac.vtp'))
print(s.NCells())
#print('labels len :', len(s.celldata['labels']))
print('labels len :', len(s.celldata['labels']))

#labels_arr = s.celldata['labels']
labels_arr = s.celldata['labels']
print(labels_arr)
#label_color_map = {'0':[254, 254, 254], '1':[252, 78, 3], '2': [252, 128, 3], '3': [252, 186, 3], '4': [252, 235, 3], '5': [231, 252, 3],\
#            '6': [198, 252, 3], '7': [161, 252, 3], '8': [57, 252, 3], '9': [3, 252, 173], '10': [3, 252, 235], '11': [3, 215, 252],\
#            '12': [3, 173, 252], '13': [3, 119, 252], '14': [177, 3, 252] }
    
#label_color_map = {'0':[254, 254, 254], '1': [252, 78, 3], '2': [3, 252, 173], '3': [252, 186, 3], '4': [3, 215, 252],\
#        '5': [3, 173, 252], '6': [198, 252, 3], '7': [177, 3, 252] }
    
#label_color_map = {'0':[254, 254, 254], '1': [252, 78, 3], '2': [3, 252, 173], '3': [252, 186, 3], '4': [3, 215, 252],\
#    '5': [92, 52, 52], '6': [198, 252, 3], '7': [177, 3, 252] }
    
#label_color_map = {'0':[254, 254, 254], '1': [252, 78, 3], '2': [3, 252, 173], '3': [252, 186, 3], '4': [3, 215, 252],\
#    '5': [212, 187, 237], '6': [198, 252, 3], '7': [177, 3, 252] }
    
#label_color_map = {'0':[254, 254, 254], '1': [252, 78, 3], '2': [3, 252, 173], '3': [252, 186, 3], '4': [3, 215, 252],\
#    '5': [91, 105, 85], '6': [198, 252, 3], '7': [177, 3, 252] }    

#label_color_map = {'0':[254, 254, 254], '1': [252, 78, 3], '2': [3, 252, 173], '3': [252, 186, 3], '4': [3, 215, 252],\
#    '5': [227, 61, 61], '6': [198, 252, 3], '7': [177, 3, 252] }  

#label_color_map = {'0':[254, 254, 254], '1': [252, 78, 3], '2': [3, 252, 173], '3': [252, 186, 3], '4': [3, 215, 252],\
#    '5': [240, 192, 238], '6': [198, 252, 3], '7': [177, 3, 252] }  

#label_color_map = {'0':[254, 254, 254], '1': [252, 78, 3], '2': [3, 252, 173], '3': [252, 186, 3], '4': [3, 215, 252],\
#    '5': [103, 166, 191], '6': [198, 252, 3], '7': [177, 3, 252] }
    
#label_color_map = {'0':[254, 254, 254], '1': [252, 78, 3], '2': [3, 252, 173], '3': [252, 186, 3], '4': [3, 215, 252],\
#    '5': [235, 227, 21], '6': [198, 252, 3], '7': [177, 3, 252] }
    
#### prospective one  9 august 2022
#label_color_map = {'0':[254, 254, 254], '1': [252, 78, 3], '2': [3, 252, 173], '3': [252, 186, 3], '4': [3, 215, 252],\
#    '5': [252, 128, 3], '6': [198, 252, 3], '7': [177, 3, 252] }
    
#label_color_map = {'0':[254, 254, 254], '1': [252, 128, 3], '2': [252, 235, 3], '3': [198, 252, 3]  , '4': [57, 252, 3] , '5': [3, 252, 235] ,\
#            '6': [3, 173, 252] , '7': [177, 3, 252]}
    
# get a nicer color map for 8 class problem
#label_color_map = {'0':[254, 254, 254], '1': [252, 128, 3], '2': [198, 252, 3], '3': [3, 252, 235]  , '4': [177, 3, 252] , '5': [3, 173, 252] ,\
#            '6': [245, 66, 179] , '7': [245, 66, 81]}

#label_color_map = {'0':[254, 254, 254], '1': [252, 128, 3], '2': [252, 235, 3], '3': [198, 252, 3], '4': [3, 252, 235]  , '5': [177, 3, 252] , '6': [3, 173, 252] ,\
#            '7': [245, 66, 179]}

#label_color_map = {'0':[254, 254, 254], '1': [252, 128, 3], '2': [252, 235, 3], '3': [198, 252, 3], '4': [3, 252, 235]  , '5': [3, 173, 252] , '6': [177, 3, 252] ,\
#                   '7': [245, 66, 179]}
    
#--------------------- current one
#label_color_map = {'0':[254, 254, 254], '1': [252, 128, 3], '2': [252, 235, 3], '3': [198, 252, 3], '4': [3, 252, 235]  , '5': [3, 173, 252] , '6': [177, 3, 252] ,\
#                   '7': [191, 8, 8]}
    
#label_color_map = {'0':[254, 254, 254], '1': [252, 78, 3], '2': [252, 128, 3], '3': [252, 235, 3], '4': [3, 252, 235]  , '5': [3, 173, 252] , '6': [177, 3, 252] ,\
#               '7': [191, 8, 8]}
    
#label_color_map = {'0':[254, 254, 254], '1': [252, 78, 3], '2': [252, 235, 3], '3':  [198, 252, 3], '4': [3, 252, 235]  , '5': [3, 173, 252] , '6': [177, 3, 252] ,\
#              '7': [191, 8, 8]}
    
#label_color_map = {'0':[254, 254, 254], '1': [156, 33, 33], '2': [219, 132, 132], '3':  [110, 176, 11], '4': [19, 120, 70]  , '5': [219, 148, 55] , '6': [28, 69, 166] ,\
#          '7': [90, 12, 153]}
    
#label_color_map = {'0':[254, 254, 254], '1': [156, 33, 33], '2': [219, 132, 132], '3':  [110, 176, 11], '4': [19, 120, 70]  , '5': [219, 148, 55] , '6': [82, 111, 191] ,\
#          '7': [90, 12, 153]}
    
label_color_map = {'0':[254, 254, 254], '1': [156, 33, 33], '2': [219, 132, 132], '3':  [110, 176, 11], '4': [19, 120, 70]  , '5': [219, 148, 55] , '6': [19, 139, 176] ,\
          '7': [90, 12, 153]}

#label_color_map = {'0':[254, 254, 254], '1': [ 157, 198, 245], '2': [92, 52, 52], '3': [44, 110, 14], '4': [157, 201, 137]  , '5': [91, 105, 85] , '6': [45, 111, 173] ,\
#                   '7': [227, 61, 61]}

#label_color_map = {'0':[254, 254, 254], '1': [ 157, 198, 245], '2': [92, 52, 52], '3': [44, 110, 14], '4': [157, 201, 137]  , '5': [142, 173, 68] , '6': [45, 111, 173] ,\
#                   '7': [227, 61, 61]}
    
#142, 173, 68
    
#### new color scheme from the paper:
#https://openaccess.thecvf.com/content/CVPR2021/papers/Hou_Exploring_Data-Efficient_3D_Scene_Understanding_With_Contrastive_Scene_Contexts_CVPR_2021_paper.pdf
'''
yellow bed - 204, 164, 53
light violet bed - 212, 187, 237
violet headstand - 121, 76, 166
brown bed - 92, 52, 52
dark green wall box - 44, 110, 14
light green floor - 157, 201, 137
hexagon table - 91, 105, 85
blue round table - 45, 111, 173
red round table - 227, 61, 61
pink rectangular table - 227, 61, 174
light pink chair  - 240, 192, 238
light blue chair - 103, 166, 191
indigo wall - 157, 198, 245
yellow rectangular table - 235, 227, 21

what about this ordering
------------------------------------
yellow bed - 204, 164, 53
light green floor - 157, 201, 137
light violet bed - 212, 187, 237
brown bed - 92, 52, 52
blue round table - 45, 111, 173
pink rectangular table - 227, 61, 174
hexagon table - 91, 105, 85

'''

#label_color_map = {'0':[254, 254, 254], '1': [204, 164, 53], '2': [157, 201, 137], '3': [212, 187, 237], '4': [92, 52, 52]  , '5': [45, 111, 173] , '6': [227, 61, 174] ,\
#                   '7': [227, 61, 61]}

  
'''
what about this ordering
------------------------------------
yellow bed - 204, 164, 53
light green floor - 157, 201, 137
light violet bed - 212, 187, 237
brown bed - 92, 52, 52
blue round table - 45, 111, 173
pink rectangular table - 227, 61, 174
dark green wall box - 44, 110, 14

'''
    
#label_color_map = {'0':[254, 254, 254], '1': [204, 164, 53], '2': [157, 201, 137], '3': [212, 187, 237], '4': [92, 52, 52]  , '5': [45, 111, 173] , '6': [227, 61, 174] ,\
#                   '7': [44, 110, 14]}
    
'''    
what about this ordering
------------------------------------
yellow bed - 204, 164, 53
light green floor - 157, 201, 137
light violet bed - 212, 187, 237
brown bed - 92, 52, 52
blue round table - 45, 111, 173
pink rectangular table - 227, 61, 174
dark green wall box - 44, 110, 14
red round table - 227, 61, 61

'''
    
#label_color_map = {'0':[254, 254, 254], '1': [204, 164, 53], '2': [157, 201, 137], '3': [227, 61, 61], '4': [92, 52, 52]  , '5': [45, 111, 173] , '6': [227, 61, 174] ,\
#                   '7': [44, 110, 14]}

    
colorlist = []    
for i in range(len(labels_arr)):
    cur_label = int(labels_arr[i])
    colorlist.append(label_color_map["{:d}".format(cur_label)])
    
print(colorlist)

#colorlist = [0]* s.NCells()
#colorlist = [[100,0,0]]*s.NCells()
#colorlist = [[0,0,0]]*s.NCells()
#colorlist = [[254,254,254]]*s.NCells()
#colorlist = [[154,154,154]]*s.NCells()
#colorlist[:10000] = [0, 0, 0]
#colorlist[:15000] = [100, 100, 100]
#colorlist = [i for i in range(s.NCells())]
#for i in range((s.NCells()//2)):
#    colorlist[i] += 100
    
#colorlist[:s.NCells()//2]
s.cellIndividualColors(colorlist)
#s.cellIndividualColors


s.show()
#