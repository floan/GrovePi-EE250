""" EE 250L Lab 02: GrovePi Sensors

List team members here. -- Just Fayez Loan. 

Insert Github repository link here. -- https://github.com/floan/GrovePi-EE250
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import *

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    PORT = 4    # D4
    rotarySensor = 0 #The rotary angle sensor is connected to A0. 
    grovepi.pinMode(rotarySensor,"INPUT") #Tells the GrovePI that we are expecting input from the rotary sensor
    time.sleep(1)

    # Reference voltage of ADC is 5v
    adc_ref = 5

    # Vcc of the grove interface is normally 5v
    grove_vcc = 5

    # Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
    full_angle = 300

    oldThreshold = -1
    oldDistance = -1

    #Initializing a variable to store text to print. This is a list with 32 entries
    textBuffer = list("   cm              cm           ")

    while True:
        try:
            time.sleep(0.2)

            #Get and store the distance from the object
            distanceInCm = grovepi.ultrasonicRead(PORT) 

            # Read sensor value from rotarySensor
            sensor_value = grovepi.analogRead(rotarySensor)

            # Calculate voltage
            voltage = round((float)(sensor_value) * adc_ref / 1023, 2)
            # Calculate rotation in degrees (0 to 300)
            degrees = round((voltage * full_angle) / grove_vcc, 2)

            thresholdLevel = int(degrees / full_angle * 517) #517 is the max range for the ultrasonic sensor

            if(thresholdLevel != oldThreshold):
                oldThreshold = thresholdLevel
                for x in range(3): #Erasing the old value 
                    textBuffer[x] = " "

                for i in range(len(str(thresholdLevel))): #Entering the new value
                    textBuffer[i] = str(thresholdLevel)[i]
                setText_norefresh("".join(textBuffer)) #Updating the LCD

            if(distanceInCm != oldDistance):
                oldDistance = distanceInCm 
                for x in range(16, 19): #Erasing the old value
                    textBuffer[x] = " "

                for i in range(len(str(distanceInCm))): #Entering the new value
                    textBuffer[i+16] = str(distanceInCm)[i]
                setText_norefresh("".join(textBuffer)) #Updating the LCD
            
            if(distanceInCm < thresholdLevel):
                textBuffer[6] = "O"
                textBuffer[7] = "B"
                textBuffer[8] = "J"
                textBuffer[9] = " "
                textBuffer[10] = "P"
                textBuffer[11] = "R"
                textBuffer[12] = "E"
                textBuffer[13] = "S"
                setText_norefresh("".join(textBuffer))
                setRGB(255,0,0)
            else:
                for x in range(6, 14):
                    textBuffer[x] = " "
                setText_norefresh("".join(textBuffer))
                setRGB(0,255,0)
                


        except KeyboardInterrupt: 
            break