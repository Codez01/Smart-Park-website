import yaml
import numpy as np
import cv2
from Detector.config import *
from Detector.ParkingRectanglesData import ParkingRectanglesData
from Detector.ParkingVideoConfig import *
from Detector.parking_detection import parking_detection
from Detector.coordinates_generator import CoordinatesGenerator
from Detector.export_reading_in_file import export_reading_in_file2 , export_reading_in_file_occupied,export_reading_in_file_occupied2

# ------------------------------------------------------------------------------------
# Gives A New Coordinates

# with open(fn_yaml2, "w+") as coors:
#   generator = CoordinatesGenerator(image, coors, (255, 0, 0))
#   generator.generate()

#-----------------------------------------------------------------------------------------------------

# Reads YAML data

parking_bounding_rects = []#rectangle coors
# it reads the coordinations
with open(fn_yaml2, 'r') as stream:
    parking_data = yaml.load(stream)

# ------------------------


ParkingRectanglesData(parking_data, parking_bounding_rects)# it puts the current coors  and draw a rectangle with them

parking_lot_state = [False] * len(parking_data)#gives the parking lot state to start with false

parking_buffer = [None] * len(parking_data)

#during the runtime of the app
while(cap.isOpened()):
    spot = 0
    occupied = 0
    array_of_free_spaces = []#array of free spaces
    array_of_occupied_spaces =[]#array of occupied spaces
# ------------------------

    # Reads the video frame-by-frame

    video_cur_pos = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0 # Current position of the video file in sec
    vv_current_frame = cap.get(cv2.CAP_PROP_POS_FRAMES) # Index of frame to be captured at the next
    playing, frame = cap.read()

# ---------------------------------------------------------------------------------------------

    if playing == False:
        print("The Second Location Has Been Scanned")# when the video finishes
        break

    # it changes the image colours to grayscale pointing out all the lines and these are the cv2 commands
    f_bluring = cv2.GaussianBlur(frame.copy(), (5,5), 3)
    f_gray = cv2.cvtColor(f_bluring, cv2.COLOR_BGR2GRAY)
    f_out = frame.copy()# the footage copy that is going to be used
#--------------------------------------------------------------------------------------

    # Detects parking rectangles and lot state
    parking_detection(parking_bounding_rects, f_gray, parking_lot_state, parking_buffer, video_cur_pos, parking_data)

# ------------------------------------------------------------------------------

    # Parking overlay
    if config['parking_lot_overlay']:
        for index, park in enumerate(parking_data):#takes the index and the parking data of each rectangle

            coors = np.array(park['coors'])#coors equals to each subset called coors in the park array from parking data


            if parking_lot_state[index]: #if the parking lot state == true
                color = (0,255,0)#green

                spot = spot + 1 #the number of the spots

                array_of_free_spaces.append(index)#add to the free spaces array
            else:
                color = (0,0,255)#red
                occupied = occupied+1 #increases the number of occupied lots
                array_of_occupied_spaces.append(index)#the array adds the places of the occupied spaces

            # Draws real rectangles
            cv2.drawContours(f_out, [coors], contourIdx=-1, color=color, thickness=2, lineType=cv2.LINE_8)

            takes = cv2.moments(coors)


            #for the font design

            cent_id = (int(takes['m10']/takes['m00'])-3, int(takes['m01']/takes['m00'])+3)

            cv2.putText(f_out, str(park['id']), (cent_id[0]+1, cent_id[1]+1), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(f_out, str(park['id']), cent_id, cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0), 1, cv2.LINE_AA)

# ------------------------------------------------------------------------------
    # displays the video
    cv2.imshow('Smart-Park', f_out)
    cv2.waitKey(1)

    # exports reading in file
    export_reading_in_file2(array_of_free_spaces)
    export_reading_in_file_occupied2(array_of_occupied_spaces)


#------------------------------------------------------------------------------

cap.release()#the cap is ended and freed
cv2.destroyAllWindows()# closes the cap