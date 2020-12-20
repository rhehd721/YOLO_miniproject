# -*- coding: utf-8 -*-
# 파일을 일정 비율로 train과 validation으로 나누는 작업압니다.

count = 0

# suffle.txt의 라인 갯수
length = 69

txt = open('/home/user/darknet/pbh/custom/suffle.txt','r')

i = 0

# train
f = open('/home/user/darknet/pbh/custom/train.txt','w')
# validation
f2 = open('/home/user/darknet/pbh/custom/validation.txt','w')

while True :
    if i == 0 :
        line = txt.readline()
        if not line :
            break
        count +=1
        # 8 : 2 비율로 나누는 작업
        if count < int(length/10)*2 :
            f2.write(line)
        else :
            f.write(line)

txt.close()
f.close()
f2.close()