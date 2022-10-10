
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


#Weather
#Developer: Kyle Rocco
#Version 1.0

"""
Create a function for our current weather using the
ranodm.choice function to determine what the weather is
picking from a list - using If, Elif and Else statements
to check the condition and print a specific print line.
"""

# Import Libraries Here
import random

#Weather condition list using the random.choice library
#to randomly choose a condition and stroing it in its brain
def weather():
    weatherForcast = ["Rain", "Snow", "Sunny", "Windy", "Foggy", "Storming", "Icy"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

weatherAlert = weather()

def vRS():
    if weatherAlert == "Icy":
        print("\nVRS has changed your alarm 30 minutes earlier based on the NWS forcast of",weatherAlert, "roads")
        print("VRS will only allow your car to go 30MPH")
    elif weatherAlert == "Snow":
        print("\nVRS has changed your alarm 15 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    elif weatherAlert == "Rain":
        print("\nVRS has changed your alarm 5 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Windy":
        print("\nVRS has changed your alarm 5 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 70MPH")
    elif weatherAlert == "Foggy":
        print("\nVRS has changed your alarm 5 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Storming":
        print("\nVRS has changed your alarm 15 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    else:
        print("\nThe weather today is,",weatherAlert,"let's Gooooo!")
        print("VRS will only allow your car to go 85MPH")
vRS()

