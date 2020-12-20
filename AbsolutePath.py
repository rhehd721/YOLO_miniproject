# -*- coding: utf-8 -*-
# 파일에 입력된 파일경로를 절대경로로 바꿔주는 코드입니다.

# 기존의 상대경로로 저장해둔 파일을 읽습니다.
txt = open('/media/gopiz/extra/vision_project/darknet/custom/train.txt', 'r')

# 새롭게 작성할 txt파일을 쓰기모드로 읽습니다.
f = open('/media/gopiz/extra/vision_project/darknet/custom/train2.txt', 'w')
while True:
    # 상대경로를 읽고
    line = txt.readline()
    if not line:
        break
    # 상대경로에 절대경로를 추가해줍니다
    f.write('/media/gopiz/extra/vision_project/Yolo_mark/' + line)

txt.close()
f.close()