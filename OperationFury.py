#Gasoline
#Programmer: Mr. Lange
#Version1.0

"""
Define a function to check our gas gauge and determine how far
we have until we need gasoline based on an if, elif, else
condition
"""

#import library here
import random

from time import sleep

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

    if gasLevelIndicator == "Empty":
        print("\033[1;31m ***WARNING YOU ARE ON EMPTY***")
        sleep(2)
        print("\nCalling Emergency Contact")

    elif gasLevelIndicator == "Low":
        print("\033[1;35m ***WARNING***")
        sleep(2)
        print("\nYour gas tank is extremely low, checking Google Maps for the closet gas station")
        sleep(1)
        print("\nThe closest gas station is", listOfGasStations(),"which is",milesToGasStationLow,"miles away.")

    elif gasLevelIndicator == "Quarter":
        print("\033[1;33m ***WARING***")
        sleep(2)
        print("\nYour gas tank is at quarter tank, checking Google Maps for the closet gas station")
        sleep(1)
        print("\nThe closest gas station is", listOfGasStations(),"which is",milesToGasStationQuarter,"miles away.")

gasLevelAlert()

