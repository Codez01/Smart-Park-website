
import cv2
from Detector.config import *
#Cap Video configiration

cap = cv2.VideoCapture(video)

video_info = {
	'fps':    cap.get(cv2.CAP_PROP_FPS),
  'width':  int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
  'height': int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
  'fourcc': cap.get(cv2.CAP_PROP_FOURCC),
  'num_of_frames': int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
}

cap.set(cv2.CAP_PROP_POS_FRAMES, config['start_frame']) # jump to frame
#*********************************************************************************************************