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

def bin2num(a):
    return a[0]*(2**7)+ a[1]*(2**6)+ a[2]*(2**5)+ a[3]*(2**4)+ a[4]*(2**3)+ a[5]*(2**2)+ a[6]*(2**1)+ a[7]
def adc():
    num=[0,0,0,0,0,0,0,0]
    time.sleep(0.005)
    for i in range(8):
        num[i] = 1
        
        signal = num2dac(bin2num(num))
        time.sleep(0.005)
        comparatorValue = GPIO.input(comp)
        #GPIO.output(dac, signal)
        if (comparatorValue == 0):
            num[i] = 0
    return bin2num(num)/levels*maxVoltage

try:
    while(True):
        print(adc())
finally:
    GPIO.output(dac,0)
    #GPIO.output(dac,0)
    GPIO.cleanup()

# def bin2num(a):
#     return a[0]*(2**7)+ a[1]*(2**6)+ a[2]*(2**5)+ a[3]*(2**4)+ a[4]*(2**3)+ a[5]*(2**2)+ a[6]*(2**1)+ a[7]
# def adc():
#     num=[]
#     for i in range(8):
#         comparatorValue = GPIO.input(comp)
#         if comparatorValue == 0:
#             num[i] = 1
#     return bin2num/levels*maxVoltage
         
