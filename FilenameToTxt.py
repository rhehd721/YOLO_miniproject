# 텍스트문서를 읽어와 그안에 파일이름을 넣어주는 코드
import os

path = '/home/user/darknet/pbh/data/'
counter = 0
# 파일이름들을 불러온뒤
fileList = os.listdir(path)

# 파일이름을 저장할 텍스트파일을 쓰기모드로 읽는다
f = open('/home/user/darknet/pbh/train.txt', 'w')

for i in fileList:

    # 파일이름을 텍스트에 넣어준다
    f.write('/home/user/darknet/pbh/data/' + i + '\n')

f.close()