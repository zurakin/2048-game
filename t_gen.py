import numpy
import cv2


font = cv2.FONT_HERSHEY_SIMPLEX

#text colors
dark = (242, 246, 249)
light = (101, 110, 119)


colors = {
2: ((104, 229 ,255),dark),
4: ((153, 204 ,255),dark),
8: ((102, 178 ,255),dark),
16: ((51, 153 ,255),dark),
32: ((0, 128 ,255),light ),
64: ((0, 102 ,204),light ),
128: ((0, 153 ,76),light ),
256: ((0, 51 ,102),light ),
512: ((0, 25 ,51),light ),
1024: ((0, 0 ,102),light ),
2045: ((0, 255 ,255),light ),
}
for num, col in colors.items():
    img = numpy.zeros((100,100,3))
    img += col[0]
    size = cv2.getTextSize(str(num), font, 1.2, 3)
    cv2.putText(img = img,text = str(num),org = (50-int(size[0][0]/2),50+int(size[0][1]/2)),fontFace = font, fontScale = 1.2,color = col[1],thickness = 3,lineType = cv2.LINE_AA)
    cv2.imwrite(str(num)+'.jpg',img)
