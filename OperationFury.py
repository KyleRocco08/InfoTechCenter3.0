
#***********************************************************************************************************************
#Import Libraries Here
from time import sleep #We imported the Sleep function from the Time Library

import random
#***********************************************************************************************************************


#Welcome Screen
#Developer: Kyle Rocco
#Version: 1.0

"""
Our Welcome Screen will Start our program letting
drivers know that the InfoTechCenter OS is Loading
"""

#("\033[3;31;40m")The \033 is the escape code. You can change 3 for different text styles, you can change 34 to change the color and change 40 for different backgroud colors

print("\033[3;31m Welcome to Operation Fury InfoTech Center")
sleep(2)

print("\033[3;34m \nOperation Fury's Operating System is Booting Up")

sleep(1.5)

for i in range(8):
    print("\033[1;36m OS Booting Up")
    sleep(1)

#Gasoline
#Programmer: Mr. Lange
#Version1.0

"""
Define a function to check our gas gauge and determine how far
we have until we need gasoline based on an if, elif, else
condition
"""

# Gas level function
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter", "Half", "Three Quarter", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Variable calling the gasLevelGauge function to store value once
gasLevelIndicator = gasLevelGauge()

def listOfGasStations():
    gasStations = ["Shell", "Circle K", "Marathon", "Speedway", "Meijer"]
    gasStationNearby = random.choice(gasStations)
    return(gasStationNearby)


def gasLevelAlert():

    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationQuarter = round(random.uniform(26, 50), 1)
    milesToGasStationHalf = round(random.uniform(51, 75), 1)

    if gasLevelIndicator == "Empty":
        print("\033[1;31m \n***WARNING YOU ARE ON EMPTY***")
        sleep(2)
        print("\nCalling Emergency Contact")

    elif gasLevelIndicator == "Low":
        print("\033[1;31m \n***WARNING***")
        sleep(2)
        print("\033[1;32m \nYour gas tank is extremely low, checking Google Maps for the closet gas station")
        sleep(1)
        print("\nThe closest gas station is", listOfGasStations(),"which is",milesToGasStationLow,"miles away.")

    elif gasLevelIndicator == "Quarter":
        print("\033[1;31m \n***WARING***")
        sleep(2)
        print("\033[1;33m \nYour gas tank is a quarter tank full, checking Google Maps for the closet gas station")
        sleep(1)
        print("\nYou need to get to this gas station", listOfGasStations(),"which is",milesToGasStationQuarter,"miles away.")

    elif gasLevelIndicator == "Half":
        print("\033[1;31m \n***Alert***")
        sleep(2)
        print("\033[1;34m \nYour gas tank is a half full, checking Google Maps for the closet gas station")
        sleep(1)
        print("\nThe closest gas station is", listOfGasStations(),"which is",milesToGasStationHalf,"miles away.")

    elif gasLevelIndicator == "Three Quarter":
        print("\033[1;31m \n***Alert***")
        sleep(2)
        print("\033[1;35m \nYour gas tank is three quarters full")
        sleep(1)
        print("You have plenty of gas left")

    else:
        print("\033[1;31m \n***Alert***")
        sleep(2)
        print("\033[1;36m \nYour gas tank is full")



#Weather
#Developer: Kyle Rocco
#Version 1.0

"""
Create a function for our current weather using the
ranodm.choice function to determine what the weather is
picking from a list - using If, Elif and Else statements
to check the condition and print a specific print line.
"""



#Weather condition list using the random.choice library
#to randomly choose a condition and stroing it in its brain
def weather():
    weatherForcast = ["Rain", "Snow", "Sunny", "Windy", "Foggy", "Storming", "Icy"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

weatherAlert = weather()

def vRS():
    if weatherAlert == "Icy":
        print("\033[1;32m \nVRS has changed your alarm 30 minutes earlier based on the NWS forcast of",weatherAlert, "roads")
        print("VRS will only allow your car to go 30MPH")
    elif weatherAlert == "Snow":
        print("\033[1;33m\nVRS has changed your alarm 15 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    elif weatherAlert == "Rain":
        print("\033[1;34m\nVRS has changed your alarm 5 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Windy":
        print("\033[1;35m\nVRS has changed your alarm 5 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 70MPH")
    elif weatherAlert == "Foggy":
        print("\033[1;36m\nVRS has changed your alarm 5 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Storming":
        print("\033[1;31m\nVRS has changed your alarm 15 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    else:
        print("\033[1;37m\nThe weather today is,",weatherAlert,"let's Gooooo!")
        print("VRS will allow your car to go 85MPH")


#***********************************************************************************************************************
#Calling functions here

gasLevelAlert()

vRS()
