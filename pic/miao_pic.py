
import cv2
import numpy as np
img = cv2.imread("/home/wy/Desktop/jumao.jpg")
# 读取
cv2.imshow("miao",img)
# 保存本地
cv2.imwrite('./miao2.jpg',img)
cv2.waitKey(10000)
cv2.destroyAllWindows()