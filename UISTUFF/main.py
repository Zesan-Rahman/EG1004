import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gpiozero import Buzzer
#from picamera import Picamera
from time import sleep
import easyocr
#import RPi.GPIO as GPIO

#Size Variables
WIDTH=600
HEIGHT=500

#Accuracy var
THRESHOLD = 0.2

# #Buzzer shit
# BUZZER_PIN = 16
# buzzer = Buzzer(BUZZER_PIN)
# buzzer.off()

#Lock shit
# LOCK_PIN = 26
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(LOCK_PIN, GPIO.OUT)

#Camera shit 
#commented bc im on windows TT
# camera = PIcamera()
# camera.rotation = 270
# #FOR TESTING
# camera.start_preview()
# camera.stop_preview()

#Initalize emergency contact list
emergencyNames = ['mom', 'dad']
# creating Tk window
root = Tk()

# setting geometry of tk window
rootSize = str(WIDTH) + "x" + str(HEIGHT)
root.geometry(rootSize)

# Using title() to display a message in
# the dialogue box of the message in the
# title bar.
root.title("Timer")

# Declaration of variables
hour=StringVar()
minute=StringVar()
second=StringVar()
name=StringVar()

# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")
name.set("")

#Entry Size Variables
hourEntryX = 80
timeEntryY = 20
timerBtnX = hourEntryX
timerBtnY = timeEntryY + 60
nameEntryX = timerBtnX
nameEntryY = timerBtnY + 60
rmNameEntryX = nameEntryX
rmNameEntryY = nameEntryY + 120

# Use of Entry class to take input from the user
hourEntry= Entry(root, width=3, font=("Arial",18,""),
				textvariable=hour)
hourEntry.place(x=hourEntryX,y=timeEntryY)

minuteEntry= Entry(root, width=3, font=("Arial",18,""),
				textvariable=minute)
minuteEntry.place(x=hourEntryX+50,y=timeEntryY)

secondEntry= Entry(root, width=3, font=("Arial",18,""),
				textvariable=second)
secondEntry.place(x=hourEntryX+100,y=timeEntryY)

nameEntry = Entry(root, width = 20, font=("Arial",18,""), textvariable=name)
nameEntry.place(x=nameEntryX, y=nameEntryY)


def addEmergencyName():
	nm = name.get()
	if (nm == '' or nm == ""):
		print("Please input valid name")
	elif(not (nm.lower() in emergencyNames)):
		emergencyNames.append(nm.lower())
		displayEmergencyContacts(WIDTH-150, 40)
	else:
		print("Contact already listed as emergency")
		
def displayEmergencyContacts(x,y):
	for contact in emergencyNames:
		temp = ttk.Label(text=contact)
		temp.place(x=x,y=y)
		y += 20

def checkCall():
	start_time = time.time()
	# camera.start_preview()
	# sleep(5)
	# camera.capture('test.jpg')
	# camera.stop_preview()
	reader = easyocr.Reader(['en'])
	result = reader.readtext('test.jpg', detail = 0)
	for i in range(len(result)):
		result[i] = result[i].lower()
	isEmergency = checkAccuracy(result)
	end_time = time.time()
	print(isEmergency)
	return (int(end_time - start_time), isEmergency)
	

def checkAccuracy(result):
	print(result)
	print(emergencyNames)
	for eName in result:
		for name in emergencyNames:
			numMatch = 0
			for i in range(len(name)):
				if (i < len(eName)):
					if (name[i] == eName[i]):
						numMatch += 1
			print(numMatch/len(name))		
			if(numMatch/len(name) >= THRESHOLD):
				return True
	return False

def submit():
	try:
		# the input provided by the user is
		# stored in here :temp
		temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
		#GPIO.output(LOCK_PIN, 1)
	except:
		print("Please input the right value")
	while (temp >-1):
		# divmod(firstvalue = temp//60, secondvalue = temp%60)
		mins,secs = divmod(temp,60) 

		# Converting the input entered in mins or secs to hours,
		# mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
		# 50min: 0sec)
		hours=0
		if mins >60:
			
			# divmod(firstvalue = temp//60, secondvalue 
			# = temp%60)
			hours, mins = divmod(mins, 60)
		
		# using format () method to store the value up to 
		# two decimal places
		hour.set("{0:2d}".format(hours))
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))

		# updating the GUI window after decrementing the
		# temp value every time
		root.update()
		time.sleep(1)

		# when temp value = 0; then a messagebox pop's up
		# with a message:"Time's up"
		info = (0, 0)
		if (temp % 5 == 0 and temp > 0):
			info = checkCall()
			temp -= info[0]
		else:
			temp -= 1
		if (temp <= 0 or info[1]):
			messagebox.showinfo("Time Countdown", "Time's up ")
			temp = -2
			#GPIO.output(LOCK_PIN, 0)
			# buzzer.on()
			# time.sleep(3)
			# buzzer.off()

# button widget
timerBtn = Button(root, text='Set Time Countdown', bd='5',
			command= submit)
timerBtn.place(x = hourEntryX,y = timeEntryY+60)

addNameBtn = Button(root, text='Add Emergency Contact', bd ='5', 
			command=addEmergencyName)
addNameBtn.place(x=nameEntryX, y= nameEntryY + 60)

#labels
EmergencyNameList = ttk.Label(text="Emergency Contacts\n(Not Case-Sensitive):")
EmergencyNameList.place(x=WIDTH-150,y=0)
displayEmergencyContacts(WIDTH-150, 40)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
root.mainloop()