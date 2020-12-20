# 훈련데이터 txt 파일을 suffle.txt에 무작위 순서로 섞습니다 본 과정은 train validation과정보다 선행되어야 합니다
import random

# 기존에 작성된 훈련데이터를 읽어온다
txt = open('/home/user/darknet/pbh/custom/train.txt', 'r')
# 새로 작성될 txt파일을 쓰기모드로 읽어온다
f = open('/home/user/darknet/pbh/custom/suffle.txt', 'w')

tmp = []

while True:
    line = txt.readline()
    if not line:
        break

    tmp.append(line)

# train의 모든데이터를 리스트로 일단 넣어준뒤 리스트를 셔플한다
random.shuffle(tmp)

# 셔플한 리스트를 한줄한줄 넣어준다
for i in tmp:
    f.write(i)

txt.close()
f.close()