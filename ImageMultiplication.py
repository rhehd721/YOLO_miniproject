# -*- coding: utf-8 -*-
from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot as plt
import os
import cv2

# 내가 읽을 폴더의 경로
path_dir = '/home/user/Desktop/img/'

# 폴더에 들어있는 파일리스트
file_list = os.listdir(path_dir)

# 파일과 파일에 해당하는 텍스트 분류
img_list = [file for file in file_list if file.endswith(".jpg")]
txt_list = [file for file in file_list if file.endswith(".txt")]

filename_in_dir = []

# 이미지파일 하나씩 불러오기
for i in range(len(img_list)):
    full_fname = os.path.join(path_dir, img_list[i])
    filename_in_dir.append(full_fname)

    name = img_list[i].split('.')

    # 이미지를 읽어온다
    img = load_img(filename_in_dir[i])

    # 이미지를 array 형태로 바꿈
    data = img_to_array(img)

    # expand를 사용하여 차원을 하나 높여준다 ( [] 추가)
    samples = expand_dims(data, 0)

    # 랜덤으로 조절할 밝기의 영역 설정
    datagen = ImageDataGenerator(brightness_range=[0.2,0.9])

    # 숫자로 변환한 이미지에 밝기값을 조정한다
    it = datagen.flow(samples, batch_size=1)

    # 이건 아직 잘 모르겠다
    batch = it.next()

    # 숫자를 다시 이미지로 바꿔준다
    image = batch[0].astype('uint8')

    cv2.imwrite('/home/user/Desktop/save/'+img_list[i], image)

######################## 여기서 다시 이미지를 읽어와야함 ############################ 
    # 밝기 변화된 이미지 읽어오기
    img = cv2.imread('/home/user/Desktop/save/'+img_list[i])

    # 상하반전 0 
    img = cv2.flip(img, 0)

    # 좌우반전 1
    img = cv2.flip(img, 1)

    cv2.imwrite('/home/user/Desktop/save/'+img_list[i], img)
######################## 반전과 밝기를 조정했다면 텍스트도 수정해줍니다. ############################ 

    # 텍스트파일 불러오기 (쓰기모드)
    f = open(path_dir+ name[0] + '.txt', 'r')
    line = f.readline()
    print(line)
    f.close()

    # # 쓰기모드
    # f = open("impo.txt", 'w')
    # # for i in range(1, 1):
    # f.write(line)
    # f.close()


    
# # 회전변수
# rotation = 0

# # 반전
# X_reversal = 0
# Y_reversal = 0

# # 밝기
# brightness = 0

# # 이동
# X_move = 0
# Y_move = 0

# # 텍스트파일 불러오기 (쓰기모드)
# f = open("impo.txt", 'r')
# line = f.readline()
# print(line)
# f.close()

# # 쓰기모드
# f = open("impo.txt", 'w')
# # for i in range(1, 1):
# f.write(line)
# f.close()

# # 이미지를 90도 회전시킵니다
# img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
