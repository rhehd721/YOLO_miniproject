# -*- coding: utf-8 -*-
# 이미지 증식시키는 참고용 코드입니다.

import math
import numpy as np
import os
from os import listdir
from os.path import isfile, join
from PIL import Image

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

# 사진 증식하는 과정

# 사진을 어떤식으로 변화줄지 설정
data_datagen = ImageDataGenerator(rescale=1. / 255,rotation_range=15,shear_range=0.5,# width_shift_range=0.1,# height_shift_range=0.1,
horizontal_flip=True,vertical_flip=True,fill_mode='nearest')


filename_in_dir = []
filename = []
j = 0

# 해당경로에서 경로와 파일들의 이름을 가져온다
for root, dirs, files in os.walk('/home/user/Desktop/img'):
    for fname in files:
        # 사진의 절대경로와 사진 하나하나의 이름을 합쳐 full_fname 이라는 리스트에 넣어준다
        full_fname = os.path.join(root, fname)
        filename_in_dir.append(full_fname)
        # 경로가 포함되지 않은 순수 파일 이름을 리스트에 넣어준다
        filename.append(fname)

# 사진파일 하나하나를 불러온다
for file_image in filename_in_dir:
    img = load_img(file_image)
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)


    i = 0

    # 사진파일 하나하나당 위에 설정한 변화를 4번 해주도록 한다
    for batch in data_datagen.flow(x, save_to_dir='/home/user/Desktop/save',
                                   save_prefix=filename[0], save_format='jpg'):
        print(x)
        j += 1
        i += 1
        if i >= 4:
            break

# 사진 좌표 구하기
point_xy = []
 
for idx in range (0, 24) :
    # y좌표
    end_y = -100
    # x 좌표
    degree = 15.0 * idx
    rad = math.pi * degree / 180.0
    new_end_x = int(-end_y * math.sin(rad))
    new_end_y = int(end_y * math.cos(rad))

    point_xy.append((new_end_x, new_end_y))
     
print(point_xy)