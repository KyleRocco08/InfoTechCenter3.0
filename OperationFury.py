#Welcome Screen
#Developer: Kyle Rocco
#Version: 1.0

"""
Our Welcome Screen will Start our program letting
drivers know that the InfoTechCenter OS is Loading
"""

#Import Libraries Here
from time import sleep #We imported the Sleep function from the Time Library

#("\033[3;31;40m")The \033 is the escape code. You can change 3 for different text styles, you can change 34 to change the color and change 40 for different backgroud colors

print("\033[3;31m Welcome to Operation Fury InfoTech Center")
sleep(2)

print("\033[3;34m \nOperation Fury's Operating System is Booting Up")

sleep(1.5)

for i in range(8):
    print("\033[1;36m OS Booting Up")
    sleep(1)

