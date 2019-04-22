# created by Huang Lu
# 27/08/2016 17:24:55
# Department of EE, Tsinghua Univ.
# 读取视频并播放
# import cv2
# import numpy as np
#
# cap = cv2.VideoCapture("./test.mp4")
# while(1):
#     # get a frame
#     # 获取frame,ret值是判断是否成功
#     ret, frame = cap.read()
#     # show a frame
#     cv2.imshow("capture", frame)
#     # print(ret)
#     if cv2.waitKey(100) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
# 读取图片并播放
# import cv2
#
# img = cv2.imread("./test.jpg")
# cv2.namedWindow("Image")
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

from PIL import Image, ImageSequence
import os
os.system("ffmpeg -i abc.mp4 -f gif test.gif")
with Image.open('test.gif') as im:
    if im.is_animated:
        frames = [f.copy() for f in ImageSequence.Iterator(im)]
        frames.reverse()
        frames[0].save('out.gif', save_all=True, append_images=frames[1:])
os.system("ffmpeg -f gif -i out.gif -vf scale=420:-2,format=yuv420p  out.mp4")