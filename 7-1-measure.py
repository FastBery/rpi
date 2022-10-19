#import 
import RPi.GPIO as GPIO
import time
import matplotlib as plt

#переменные
dac = [26,19,13,6,5,11,9,10]
comp = 4
troyka = 17
maxVoltage = 3.3
levels = 256
led = [21,20,16,12,7,8,25,24]

#настройка GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)
GPIO.setup(led,GPIO.OUT)

    #fuctions
#10_to_2
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
#num2dac
def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac,signal)
    return signal
#2_to_10
def bin2num(a):
    return a[0]*(2**7)+ a[1]*(2**6)+ a[2]*(2**5)+ a[3]*(2**4)+ a[4]*(2**3)+ a[5]*(2**2)+ a[6]*(2**1)+ a[7]

def adc():
    num=[0,0,0,0,0,0,0,0]
    time.sleep(0.005)
    for i in range(8):
        num[i] = 1
        signal = num2dac(bin2num(num))
        time.sleep(0.004)
        comparatorValue = GPIO.input(comp)
        #GPIO.output(dac, signal)
        if (comparatorValue == 0):
            num[i] = 0
    r = bin2num(num)/levels*maxVoltage
    for i in range(8):
        if(num[i]==1):
            num[i]=0
            for j in range(i+1,8):
                num[j]=1
            break
    print(num)
    GPIO.output(led,num)
    time.sleep(0.1)
    return r
data = []
time_array = []
try:
    GPIO.output(troyka,1)
    t = time.time()
    while(adc()<0.97*3.3):
        data.append(adc())
    GPIO.output(troyka,0)
    time_charged = time.time()
    while(adc()>0.05*3.3):
        data.append(adc())
    time_uncharged = time.time()
    for i in range(len(data)):
        time_array[i] = (time_uncharged - t)/len(data)*i
    plt.plot(data,time_array)
    plt.show()
    with open('data.txt','w') as f:
        for i in data:
            f.write(str(i))
finally:
    GPIO.output(dac,0)
    GPIO.output(led,0)
    GPIO.cleanup()