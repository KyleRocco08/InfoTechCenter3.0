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
    weatherForcast = ["Rain", "Snow", "Sunny", "Cloudy", "Foggy", "Storming", "Icy"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition




