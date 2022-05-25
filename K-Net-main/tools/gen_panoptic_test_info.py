import mmcv

data_root = 'D:/Decision/Knet/K-Net-main/annotations'

#val_info = mmcv.load(f'{data_root}/panoptic_val2017.json')
#test_old_info = mmcv.load(f'{data_root}/image_info_test-dev2017.json')
val_info = mmcv.load(f'{data_root}/image_info_test2017.json')
test_old_info = mmcv.load(f'{data_root}/image_info_test-dev2017.json')
test_info = test_old_info
test_info.update({'categories': val_info['categories']})
mmcv.dump(test_info, f'{data_root}/panoptic_image_info_test-dev2017.json')
