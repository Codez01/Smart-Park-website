from flask import Flask, render_template, request
from twilio.rest import Client#API for sms
import requests


#file opening for counter free parking spots and counting them ~
from werkzeug.utils import redirect

#first location
file = open("C:/Users/nopro/PycharmProjects/pythonProject11/Reading_And_Assets/reading.txt", "r")
data = file.read()
words = data.split()
FreeSpaceCounter = len(words)
file.close()

file = open("C:/Users/nopro/PycharmProjects/pythonProject11/Reading_And_Assets/reading.txt", "r")
FreeSpace =file.read()

file = open("C:/Users/nopro/PycharmProjects/pythonProject11/Reading_And_Assets/reading_occ.txt", "r")
data = file.read()
words = data.split()
OccupiedSpaceCounter = len(words)
file.close()
file = open("C:/Users/nopro/PycharmProjects/pythonProject11/Reading_And_Assets/reading_occ.txt", "r")
OccupiedSpace =file.read()


#second location
file = open("C:/Users/nopro/PycharmProjects/pythonProject11/Reading_And_Assets/reading2.txt", "r")
data = file.read()
words = data.split()
FreeSpaceCounter2= len(words)
file.close()
file = open("C:/Users/nopro/PycharmProjects/pythonProject11/Reading_And_Assets/reading2.txt", "r")
FreeSpace2 =file.read()

file = open("C:/Users/nopro/PycharmProjects/pythonProject11/Reading_And_Assets/reading2_occ.txt", "r")
data = file.read()
words = data.split()
OccupiedSpaceCounter2= len(words)
file.close()
file = open("C:/Users/nopro/PycharmProjects/pythonProject11/Reading_And_Assets/reading2_occ.txt", "r")
OccupiedSpace2 =file.read()

def sms():#sms sending function for the first location
    account_sid = 'AC52cc3fe00fba098f0e4da47fc2a0a9cb'
    auth_token = 'bc541ba7223c887d44a142bcd4d94200'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"Free Parking Spot Detected In The First Location\nSpots Are :{FreeSpace} ",
        from_='+14124192661',
        to='+972527099287'
    )

    print(message.sid)

def sms2():#sms sending function for the second location
    account_sid = 'AC52cc3fe00fba098f0e4da47fc2a0a9cb'
    auth_token = 'bc541ba7223c887d44a142bcd4d94200'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"Free Parking Spot Detected In The Second Location\nSpots Are :{FreeSpace2} ",
        from_='+14124192661',
        to='+972527099287'
    )

    print(message.sid)



#------------------------------------------------------------------------------------------------

from flask import url_for

app = Flask(__name__)

@app.route('/' , methods=['GET', 'POST'])

def Home():

 return render_template('index.html')




@app.route('/firstLoc' , methods=['GET', 'POST'])
def FirstLoc():


    if request.method == "POST":# the button has been pressed
        text_file = open("Reading_And_Assets/Pressed.txt", "w")
        text_file.write("Pressed")
        text_file.close()



        return render_template('index2.html', FreeSpaceCounter=FreeSpaceCounter, FreeSpace=FreeSpace,
                               OccupiedSpaceCounter=OccupiedSpaceCounter, OccupiedSpace=OccupiedSpace)



    return render_template('index2.html' ,FreeSpaceCounter =FreeSpaceCounter , FreeSpace=FreeSpace
                           ,OccupiedSpaceCounter= OccupiedSpaceCounter,OccupiedSpace=OccupiedSpace)






@app.route('/secLoc',  methods=['GET', 'POST'])
def SecLoc():
    if request.method == "POST":# the button has been pressed
        text_file = open("Reading_And_Assets/Pressed2.txt", "w")
        text_file.write("Pressed")
        text_file.close()



        return render_template('index3.html', FreeSpaceCounter=FreeSpaceCounter2, FreeSpace=FreeSpace2,
                               OccupiedSpaceCounter=OccupiedSpaceCounter2, OccupiedSpace=OccupiedSpace2)


    return render_template('index3.html' ,FreeSpaceCounter =FreeSpaceCounter2 , FreeSpace=FreeSpace2 ,
                           OccupiedSpaceCounter= OccupiedSpaceCounter2,OccupiedSpace=OccupiedSpace2)

app.debug=True
app.jinja_env.auto_reload = True #auto page refresher
if __name__ == '__main__':


    app.run()





