import os
import time
from Flask import sms ,sms2
from Flask import FreeSpaceCounter ,FreeSpaceCounter2
from multiprocessing import Process

#*****************************************SERVER-SIDE*******************************************************
#----------------------------------------------------------------------------------------------------
def RunFirstLocation():

    os.system('cmd /c "python firstLoc.py --mode 3"')# for running args command for running the first location

def RunSecondLocation():

    os.system('cmd /c "python SecondLoc.py --mode 2"')# for running args command for running the second location


#----------------------------------------------------------------------------------------------------
os.chdir(os.path.dirname(os.path.abspath(__file__)))#makes sure that the app is gonna load the same folders,files


#**********************for the first location**********************

file = open("Reading_And_Assets/Pressed.txt", "r")
data = file.read()

if(data == "Pressed" and FreeSpaceCounter!=0 ):
# if the data == pressed from html request it will send an sms when there is a free parking lot available
    sms()
    text_file = open("Reading_And_Assets/Pressed.txt", "w")
    text_file.write("Not-Pressed")
    text_file.close()

#***********************for the second location*********************

file = open("Reading_And_Assets/Pressed2.txt", "r")
data2 = file.read()
if (data2 == "Pressed" and FreeSpaceCounter2 != 0):
# if the data == pressed from html request it will send an sms when there is a free parking lot available
    sms2()
    text_file = open("Reading_And_Assets/Pressed2.txt", "w")
    text_file.write("Not-Pressed")
    text_file.close()

#--------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    p1= Process(target = RunFirstLocation())
    p2= Process(target = RunSecondLocation())
    p1.start()
    p2.start()

    p1.join()
    p2.join()

#runs the two location at the same time using threads or multi8proccessing