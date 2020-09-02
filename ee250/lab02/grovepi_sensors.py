""" EE 250L Lab 02: GrovePi Sensors

List team members here.

Insert Github repository link here.
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
    potentiometer = 0 #The rotary angle sensor is connected to A0. 
    grovepi.pinMode(potentiometer,"INPUT") #Tells the GrovePI that we are expecting input from the potentiometer
    time.sleep(1)

    # Reference voltage of ADC is 5v
    adc_ref = 5

    # Vcc of the grove interface is normally 5v
    grove_vcc = 5

    # Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
    full_angle = 300

    #Defining the max range as 517 (max for the ultrasonic range)
    MAX_RANGE = 517

    #Initializing an variable to later compare and see if the threshold has been changed
    oldThreshold = -1

    #Initializing a variable to store text to print
    textToPrint = ""

    while True:
        try:
            #So we do not poll the sensors too quickly which may introduce noise,
            #sleep for a reasonable time of 200ms between each iteration.
            time.sleep(0.2)

            # print(grovepi.ultrasonicRead(PORT)) #This will get me the distance to the object. 

            """
            	Things to do: 
            	1. Allow the rotary encoder to change the threshold value
            	2. Poll the distance to the object 
            	3. Find out if the distance passes the threshold value 
            	4. Print to the LCD the value, whether the object is present or not and current distance
            	5. (Optional) Change the color of the LCD when it passes the threshold level.
            """

            #Get and store the distance from the object
            distanceInCm = grovepi.ultrasonicRead(PORT) 

            # Read sensor value from potentiometer
            sensor_value = grovepi.analogRead(potentiometer)

            # Calculate voltage
            voltage = round((float)(sensor_value) * adc_ref / 1023, 2)
            # Calculate rotation in degrees (0 to 300)
            degrees = round((voltage * full_angle) / grove_vcc, 2)

            # Calculate LED brightess (0 to 255) from degrees (0 to 300)
            thresholdLevel = int(degrees / full_angle * 517)

            if(thresholdLevel != oldThreshold):
                oldThreshold = thresholdLevel
                textToPrint.join(str(thresholdLevel))



        except KeyboardInterrupt: 
            break






















