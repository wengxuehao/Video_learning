""" 从视频读取帧保存为图片"""
import cv2

cap = cv2.VideoCapture("./test.mp4")#名为'003.mp4'的文件
c=0                             #文件名从0开始
while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)
    cv2.imwrite('image/'+str(c) + '.jpg',frame) #存储为图像
    c=c+1
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
