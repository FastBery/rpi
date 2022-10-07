import RPi.GPIO as GPIO
import time
dac = [26,19,13,6,5,11,9,10]
comp = 4
troyka = 17
maxVoltage = 3.3
levels = 256
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac,signal)
    return signal
def adc():
    for value in range(256):
        time.sleep(0.005)
        signal =num2dac(value)
        voltage = value/levels*maxVoltage
        time.sleep(0.0001)
        comparatorValue = GPIO.input(comp)
        if (comparatorValue == 0):
            return voltage
            break
try:
    while(True):
        print(adc())
finally:
    GPIO.output(dac,0)
    #GPIO.output(dac,0)
    GPIO.cleanup()