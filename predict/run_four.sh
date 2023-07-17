#!/usr/bin/env bash


exp_name='pointnet'
for exp_name in 'pointnet' 'pointnet2' 'dgcnn' 'meshsegnet' 'mmnet' 'pointmlp' 'pct' 'mbesegnet' 'gac' 'tsgcn'
do
#python predict_on_test_set_3dteethseg_molar.py --network ${exp_name}
python predict_on_test_set_3dteethseg_four_teeth.py --network ${exp_name}

done
