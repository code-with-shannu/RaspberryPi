import RPi.GPIO as GPIO
import time

LedPin = 13

def SetUp():
    #declare the mode of the gpio whether it is GIPO.BOARD or GPIO.BCM
    GPIO.setmode(GPIO.BCM)
    #GPIO.BCM uses the number followed by 'GPIO' number of pin
    #whereas GPIO.BOARD uses the pin number
    GPIO.setup(LedPin,GPIO.OUT,initial = GPIO.HIGH)
    #this sets the pin number 13 as output and initially it is high

def main():
    while True:            
        print("LED ON")
        GPIO.output(LedPin,GPIO.HIGH)
        time.sleep(5)
        print("LED OFF")
        GPIO.output(LedPin,GPIO.LOW)
        time.sleep(10)

def destroy():
    #Turns off
    GPIO.output(LedPin,GPIO.LOW)
    GPIO.cleanup()# this clears the resource
    
#If i start running this scrip directly it starts from here:
if __name__== '__main__':
    SetUp()
    try:
        main()
    #When ctrl+c is pressed ,this program executes destroy function 
    except KeyboardInterrupt:
        destroy()    