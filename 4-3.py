import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac=[26,19,13,6,5,11,9.10]
GPIO.setup(dac,GPIO.OUT)
GPIO.output(dac,1)
GPIO.setup(24,GPIO.OUT)
p = GPIO.PWM(24,1000)
p.start(0)
cycle = 0
try:
    while True:
        cycle = int(input())
        print(3.3*cycle/100)
        p.start(cycle)
finally:
    p.start(0)
    GPIO.cleanup()