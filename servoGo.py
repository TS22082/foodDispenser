import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

def servoGo ():

    svo1 = GPIO.PWM(2, 50)
    svo2 = GPIO.PWM(4, 50)

    svo1.start(0)
    svo2.start(0)

    svo1.ChangeDutyCycle(12.5)#dutycycle also 2.5, 7.5, and 12.5
    svo2.ChangeDutyCycle(12.5)

    time.sleep(.75) #servo function time

    svo1.ChangeDutyCycle(0)# servo off,
    svo2.ChangeDutyCycle(0)

servoGo()
