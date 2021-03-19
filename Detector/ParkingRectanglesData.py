import numpy as np
import cv2

# for inbounding rectangle Coordinations
def ParkingRectanglesData(parking_data, parking_bounding_rects):
	for park in parking_data:
#parking_data is the array contaning each coordination ID and its Coordinations under the name 'coors'
	    coors = np.array(park['coors']) # numpy array used for less memory consumption and fast perf
	    rect = cv2.boundingRect(coors) # for making a rectangle for the specified Coordinations
	    parking_bounding_rects.append(rect)