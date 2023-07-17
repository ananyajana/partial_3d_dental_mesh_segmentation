#!/usr/bin/env bash


exp_name='pointnet'
#for exp_name in 'pointnet' 'pointnet2' 'dgcnn' 'meshsegnet' 'mmnet' 'pointmlp' 'pct' 'mbesegnet' 'gac' 'tsgcn'
for exp_name in 'pointnet' 'pointnet2' 'dgcnn'  'pointmlp' 'pct' 
do
#python predict_on_test_set_3dteethseg_molar.py --network ${exp_name}
python predict_on_test_set_3dteethseg_half_jaw.py --network ${exp_name}

done
