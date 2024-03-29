import RPi.GPIO as gpio
import time 

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(23,gpio.OUT)
    gpio.setup(24,gpio.OUT)

def forward(sec):
        init()
        gpio.output(17,True)
        gpio.output(22,False)
        gpio.output(23,True)
        gpio.output(24,False)
        time.sleep(sec)
        gpio.cleanup()


def backward(sec):
        init()
        gpio.output(17,False)
        gpio.output(22,True)
        gpio.output(23,False)
        gpio.output(24,True)
        time.sleep(sec)
        gpio.cleanup()
def stop():
        init()
        gpio.output(17,False)
        gpio.output(22,False)
        gpio.output(23,False)
        gpio.output(24,False)
        gpio.cleanup()


while True:
    comm= input("f-forward,b-backward,s-stop") 
    duration=int(input("kindly enter duration(secs)>> "))
    if (comm=="f"):
        forward(duration)
    elif (comm=="b"):
       backward(duration)
    else:
       stop()




