from PIL import Image, ImageSequence
import os
# 原视频转换成gif
os.system("ffmpeg -i /home/wy/Desktop/Video_learning/video/test.mp4 -f gif test.gif")
with Image.open('test.gif') as im:
    if im.is_animated:
        frames = [f.copy() for f in ImageSequence.Iterator(im)]
        frames.reverse()
        frames[0].save('out.gif', save_all=True, append_images=frames[1:])
# 新的gif转换成新的翻转MP4
os.system("ffmpeg -f gif -i /home/wy/Desktop/Video_learning/out.gif -vf scale=420:-2,format=yuv420p  out.mp4")
