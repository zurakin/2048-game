import numpy as np
import cv2


#create a brown background
bg = np.zeros((500,500,3))
# bg += (202,165,62)
bg += (168, 173, 184)

#add borders to the background
for line in range(5):
    cv2.line(bg,(line * 120+10,0),(line*120 +10, 500),(0,51,102),20)

for column in range(5):
    cv2.line(bg,(0,column * 120+10),(500, column * 120+10),(0,51,102),20)

#export image:
cv2.imwrite('background.png',bg)
