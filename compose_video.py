import numpy as np
import cv2
import glob
import os

list_frames = sorted(glob.glob('/home/arch/GIT/ESRGAN_upscale_video//results/*.jpg'), key=os.path.getmtime)

# get size only 1 time
height, width, _ = cv2.imread(list_frames[0]).shape
size = (width,height)

img_array = []
for filename in list_frames:
    img = cv2.imread(filename)
    img_array.append(img)
    #print(filename)

out = cv2.VideoWriter('results/videoHR.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

length = len(img_array)
for i in range(length):
	print(i, length)
	out.write(img_array[i])

out.release()