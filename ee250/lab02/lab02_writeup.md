4.1:

cd my-imaginary-repo
touch my_second_file.py
git add my_second_file.py
git commit -m "Added a second file"
git push

4.2: 
I developed on my VM and pushed the files to github. I pulled them in my rpi and ran the programs from there. The main problem I faced was rewriting the add/commit/push commands for each minor change I made. In order to get past that I wrote a bash function to automate it. That definitely helps but I think I will also learn vi (I tried nano but it was just horrible).

4.3: 
There is a constant delay because the firmware for the ultrasonic sensor has a time delay of 50ms. We wait for 60ms in the ultrasonicRead function. That (60ms) is the total delay time. Additionally, the RPI uses the I2C communication protocol. 

