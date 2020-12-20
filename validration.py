import random

txt = open('/media/gopiz/extra/vision_project/darknet/custom/train2.txt','r')
f = open('/media/gopiz/extra/vision_project/darknet/custom/train_suffle.txt','w')

tmp = []

while True :
    line = txt.readline()
    if not line:
        break
        
    tmp.append(line)
    
random.shuffle(tmp)
        
for i in tmp :  
    f.write(i)

txt.close()
f.close()