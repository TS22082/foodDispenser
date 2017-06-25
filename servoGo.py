import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

def servoGo ():

    s = GPIO.PWM(2, 50)
    n = GPIO.PWM(4, 50)

    s.start(0)
    n.start(0)

    s.ChangeDutyCycle(12.5)#dutycycle also 2.5, 7.5, and 12.5
    n.ChangeDutyCycle(12.5)

    time.sleep(.75) #servo function time

    s.ChangeDutyCycle(0)# servo off,
    n.ChangeDutyCycle(0)

servoGo()
