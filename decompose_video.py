import numpy as np
import cv2
import time

# 0.0166 # 60 fps
# 0.0333 # 30 fps
fps = 0.004
cap = cv2.VideoCapture('videosLR\\video.mp4')
t = time.time()

i = 0
while(True):
	ret, frame = cap.read()
	if np.float64(time.time() - t) >= np.float64(fps):
		#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		if ret == True:
			t = time.time()
			i += 1
			cv2.imwrite("LR\\" + str(i) + ".jpg", frame)
		else:
			break