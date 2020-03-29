# class rectangle:
# def __init__(self, width, height, color):
#self.width = width
#self.height = height
#self.color = color
#self.area = width * height

# Define blob as a class with speed, power, and fight/flight response
import numpy as np

import pprint
import time


class Location:
    """Location of a object
    """

    def __init__(self, x, y):
        """Location of an object

            Arguments:
                x {Integer} -- X coordinate of a thing
                y {Integer} -- Y coordinate of a thing
            """
        self.x = x
        self.y = y


class Blob:
    """A blob that acts a player in game theory tests
    """

    def __init__(self, speed, power, fight, location, size):
        """A Blob that acts as a player in a game theroy test

            Arguments:
                speed {[Array]} -- A x and y component of velocity
                power {Integer} -- Rate of energy consumed per turn
                fight {[Boolean]} -- Fight or flight: does the blob fight or flee from confrontation?
                location {[Location]} -- Location of the blob
            """
        self.speed = speed
        self.power = power
        self.fight = fight
        self.location = location
        self.size = size
    def updateLocation(self,location):
        """Updates location of blob
        
        Arguments:
            location {Location} -- New location for blob
        """
        self.location = location 

class Food:
    """Designates food propertis of objects, currenlty a unique value, could eventually be a part of blobls when it's time to simulate carnivorous blobs
    """

    def __init__(self, energy, location, energyDensity):
        """Designates food propertis of objects, currenlty a unique value, could eventually be a part of blobls when it's time to simulate carnivorous blobs

            Arguments:
                energy {Integer} -- Energy value of consuming food
                location {Location} -- An object that gives the x and y coordinates of the food
            """
        self.energy = energy
        self.location = location
        self.energyDensity = energyDensity
        self.size = self.energy * energyDensity # Energy densety

    def print(self):
        print(" location ", self.location.x," ", self.location.y ," energy ", self.energy)


# This is effectively the core module code of the program. This will run continously?
# Randomly generate locations for N number of food, N=15 here.
if __name__ == "__main__":

    # Generates locations and energy values for different food objects, outputs list as foodlist
    foodCount = 15
    locationx = np.random.uniform(-20, 20, foodCount)
    locationy = np.random.uniform(-20, 20, foodCount)
    energyValue = np.random.uniform(2, 0.5, foodCount)

    foodList = []
    for i in range(0, foodCount):
        loc = Location(locationx[i], locationy[i])
        energyDensity = 0.1
        foodList.append(Food(energyValue[i], loc, energyDensity))

    # Define the starting number of blobs, this should be an input with foodcount when this all becomes a function!!!
    blobCount = 5

    # Define the speeds of each blob
    topSpeed = 3 # units/time
    minSpeed = 0.5 # units/time
    blobSpeeds = np.random.uniform(topSpeed,minSpeed,blobCount)

    # Define the sizes of each blob, these will also need to be function inputs
    maxSize = 1.5
    minSize = 0.25
    blobSizes = np.random.uniform(minSize,maxSize,blobCount)
    

    # Define the starting positions of the blobs
    blobLocationX = np.random.uniform(-20, 20, blobCount)
    blobLocationY = np.random.uniform(-20, 20, blobCount)
    blobList = []

    # Define power
    # power = size * speeds^2

    # Make all the blobs
    for i in range(0, blobCount):
        loc = Location(blobLocationX[i], blobLocationY[i])
        # TODO: Add speed, power, fight (fight or flight), size
        # Define fight
        fightOrFlight = np.random.random(1)[0] > 0.5
        # Define power as size (times speed^2)/time
        power = blobSizes[i] * blobSpeeds[i]
        blobList.append(Blob(blobSpeeds[i],power,fight,Location(blobLocationX, blobLocationY), blobSizes[i]))



    # Define the size of the time tics 
    # Experiment length (periods) 
    periods = 200
    tics = periods / max(blobSpeeds)

    # Define the function that determines the traveling direction of the blobs
    # Define reproduction function
    # Define aggression function
    # Add a size function to the blobs, this will determine how close the food the blob must get to "consume" it


    # Food distribution rule
        # If more than one blob reaches food in the same tick the outcome depends on fighty/flight matix: 
        # If all "fight = False", then each gets food.energy/N for N blobs at food
        # If at least 1 is "fight = True" then all flights run away with no food
        # If more than 1 fight, then the "winner" is randomly selected and the other "fighters" die

   
        

