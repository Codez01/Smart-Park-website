import argparse


#command lines

# Detect mode
parser = argparse.ArgumentParser(description='Parking lot')
parser.add_argument("--mode", dest="Test_Number", required=True)
parser = parser.parse_args()

# Test mode
Test_Number = parser.Test_Number

# Test videos
video = "datasets/videos/parking_" + Test_Number + ".mp4"


# Test Images
image = "datasets/images/parking_" + Test_Number + ".png"


# Saving coordinates of user mouse clicks
fn_yaml = "datasets/parking_yaml.yml"
fn_yaml2 = "datasets/parking_yaml2.yml"

#----------------------------------------------------------------------------------------------

# main project configuration
config = {
  'parking_lot_overlay': True,
  'parking_detection': True,
  'min_area_motion_contour': 60,
  'park_sec_to_wait': 3,
  'start_frame': 0
}