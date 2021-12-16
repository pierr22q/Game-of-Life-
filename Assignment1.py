#Qiana Pierre 04/02/2020 Assigment1
#Description:  a Python program for a one-dimensional version of the ​Game of Life​.
# The basic idea of the Game of Life is that cells in a grid are used to simulate
# biological cells. Each cell is either alive or dead
# Attribution for any sources: geeksforgeeks , Ruth for clarfiication of assignment, Fatima

import copy
import random

def advanceTime(lifeList):
    """
    copy the list, traverse the list and make changes in the copy as required by the rules
    return the new version of the array, using the returned value to overwrite the prior value
    """

    lifeList2 = copy.copy(lifeList) # copy of lifeList where changes will be made
    for i in range(0,len(lifeList)-1): # this goes thorough the index list
        if isZero(lifeList,i) == False and shouldDie(lifeList,i) == True: # two live neighboors
                lifeList2[i] = 0 # kill index i
        elif  isZero(lifeList,i) == False and shouldDie(lifeList,i) == False: # one or both neighboor is dead
                if lifeList[i + 1] == 0: #checking neighboor in front of index i
                    lifeList2[i + 1] =  1 # making dead neighboor alive
                elif lifeList[i - 1] == 0: # checking neighboor behind index i
                    lifeList2[i - 1] = 1 # making dead neighboor alive
    return lifeList2

def isZero(lifeList2,i):
    """ takes a list and an index ​i​ as parameters.
     It returns true if the element at position ​i​ is zero,
      otherwise returns false. """

    if lifeList2[i] == 0:
        return True # element at position i is 0
    else:
        return False # element at position i is not 0

def shouldDie(lifeList2,i):

    """  takes a list and an index ​i​ as parameters.
     It returns True if both neighbors of the element at
     index ​i​ have value 1; otherwise it returns False   """

    if i != 0 and i != len(lifeList2) - 1 : # not a index 1 nor the last index
        if lifeList2[i - 1] == 1 and lifeList2[i + 1] == 1: # both neighboors are alive = 1
            return True  # both neighbors are alive = 1 -> death of i
    return False # one or two dead neighbor cells

def RandomList(NUM_ELEMENTS,lifeList):
    """
    takes the size of the Game of Life  (NUM_ELEMENTS_) and a list.
    It creates and returns a random list of size (NUM_ELEMENTS)
    """
    for i in range(0,NUM_ELEMENTS):
        add = random.randint(0,1)
        lifeList.append(add)
    return(lifeList)


def main():
    lifeList = [] #empty list
    NUM_TIME_STEPS = 10 # how many “generations” the simulation will run for
    NUM_ELEMENTS = 10 # the size of the Game of Life list
    print("=== Initial Values ===")
    print(RandomList(NUM_ELEMENTS,lifeList))
    for i in range(0,NUM_TIME_STEPS):
        print("=== Values after" , i + 1, " " + "timesteps ===")
        print(advanceTime(lifeList))
        lifeList.clear()
        (RandomList(NUM_ELEMENTS,lifeList))



main()
