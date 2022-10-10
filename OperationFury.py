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

# Gas level function
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter", "Half", "Three Quarter", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

