import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac=[26,19,13,6,5,11,9.10]
GPIO.setup(dac,GPIO.OUT)

def binary(a):
    return [int(d) for d in bin(a)[2::].zfill(8)]

d=0
try:
    while True:
        t=int(input())
        while d!=255:
            GPIO.output(dac,binary(d))
            time.sleep(t/512)
            d+=1
        while d!=0:
            GPIO,output(dac,binary(d))
            time.sleep(t/512)
            d-=1

finally:
    GPIO.setup(dac,0)
    GPIO.cleanup()