import RPi.GPIO as GPIO
dac=[26,19,13,6,5,11,9.10]
GPIO.setmode(GPIO.BCM)
[GPIO.setup(el,GPIO.OUT) for el in dac]

def binary(a):
    return [int(el) for el in bin(a)[2::].zfill(8)]

try:
    while True:
        num = input()
        if num == 'q':
            break
        if num.isdigit() and 0<=255:
            a = binary(int(num))
            [GPIO.output(dac[el],a[el] for el in rasnge(8))]
            volts = int(num)/256*3.3
            print(volts,"B")
        else:
            print("Введите целое число от 0 до 255")

finally:
    [GPIO.output(el,0) for el in dac]
    GPIO.cleanup()