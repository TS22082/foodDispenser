from flask import Flask, render_template

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/o')
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

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')
