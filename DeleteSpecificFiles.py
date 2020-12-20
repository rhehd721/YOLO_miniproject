# 특정 확장자 파일 삭제하기

import os
import glob

path = '~/Desktop/img'

# 확장자가 txt인 파일을 찾아 삭제한다
for f in glob.glob("/home/user/Desktop/img/*.txt"):
    os.remove(f)
