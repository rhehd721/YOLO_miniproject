# -*- coding: utf-8 -*-
# 파일의 이름을 바꿔주는 코드입니다

import os

# 바꿀 사진의 경로
path = '/Users/alpaka/Desktop/YOLO_dataset/dataset/obj/'
counter = 0

# 피일들을 불러오고
fileList = os.listdir(path)
# print(len(fileList))

for filename in fileList:
    # image path
    srcpath = os.path.join(path, filename)

    # 딱히 쓸일없는 코드
    # name = filename.split(".")

    if (counter < 10):
        dstname = 'obj_00'+ str(counter) + ".jpg"
        dstpath = os.path.join(path, dstname)
    else:
        dstname = 'obj_0'+ str(counter) + ".jpg"
        dstpath = os.path.join(path, dstname)

    os.rename(srcpath, dstpath)

    counter = counter + 1