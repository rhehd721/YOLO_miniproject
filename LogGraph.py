# YOLO 학습중 만들어진 log파일을 그래프로 보는 방법

import sys
import matplotlib.pyplot as plt
from tqdm import tqdm

lines = []
for line in tqdm(open('/media/gopiz/extra/vision_project/darknet/backup/train.log')):
    if "avg" in line:
        lines.append(line)

iterations = []
avg_loss = []
line_cnt=len(lines)

for i in tqdm(range(line_cnt)):
    lineParts = lines[i].split(',')
    iterations.append(int(lineParts[0].split(':')[0]))
    avg_loss.append(float(lineParts[1].split()[0]))

fig ,ax  = plt.subplots(2,1 , figsize = (10,10))

#start = 0
start = 4999


for i in range(start, line_cnt, 1000):
    ax[0].plot(iterations[i:i+1], avg_loss[i:i+1], 'r*-')
    #print(iterations[i], avg_loss[i])
    ax[0].text(iterations[i], avg_loss[i],str(iterations[i]))

ax[0].set_xlabel('Iteration Number')
ax[0].set_ylabel('Avg Loss')
ax[0].set_title('loss graph')

for i in range(line_cnt-3000,line_cnt,):
    ax[1].plot(iterations[i:i+2], avg_loss[i:i+2], 'r.-')

ax[1].set_xlabel('Iteration Number')
ax[1].set_ylabel('Avg Loss')
ax[1].set_title('Recent 3000')
#fig.savefig('training_loss_plot.png', dpi=1000)