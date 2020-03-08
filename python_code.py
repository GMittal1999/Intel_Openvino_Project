#IMPORTING ALL THE NECESSARY LIBRARIES

from flask import Flask
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)  #Setting the pinMode of the Raspberrypi  as BOARD
m1=32  #Motor1 Enable
m2=15  #Motor2 Enable
d11=7  #Motor1 Int1
d12=11 #Motor1 Int2
d21=13 #Motor2 Int3
d22=15 #Motor2 Int4

#SETTING ALL THE GPIO PINS AS OUTPUT

GPIO.setup(m1,GPIO.OUT)
GPIO.setup(m2,GPIO.OUT)
GPIO.setup(d11,GPIO.OUT)
GPIO.setup(d12,GPIO.OUT)
GPIO.setup(d21,GPIO.OUT)
GPIO.setup(d22,GPIO.OUT)

#FORMING A FLASK OBJECT

app=Flask(__name__)

#DEFINING THE ROUTES

@app.route('/')
def index():
	return ''
@app.route('/forward')    #For car to move  in forward direction
def f():
	GPIO.output(m1,True)
	GPIO.output(m2,True)
	GPIO.output(d11,True)
	GPIO.output(d12,False)
	GPIO.output(d21,False)
	GPIO.output(d22,True)
	return 'forward'
@app.route('/backward')   #For car to move in forward direction
def b():
	GPIO.output(m1,True)
        GPIO.output(m2,True)
        GPIO.output(d11,False)
        GPIO.output(d12,True)
        GPIO.output(d21,True)
        GPIO.output(d22,False)
	return 'backward'

@app.route('/left')  #For car to move in Left
def l():
	GPIO.output(m2,True)
	GPIO.output(d21,False)
	GPIO.output(d22,True)
	return 'left'

@app.route('/right')  #For car to move in right
def r():
	GPIO.output(m1,True)
	GPIO.output(d11,True)
	GPIO.output(d12,False)
	return 'right'

@app.route('/stop')   #For car to stop
def s():
	GPIO.output(m1,False)
	GPIO.output(m2,False)
	return 'stop'
if __name__=='__main__':
	app.run(host='0.0.0.0')  #Running our flask Server
