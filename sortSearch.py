# sorting and searching functions
import random

class Sort():
    # a sorting class containing sorting for bubble, merge, heap and quick
    def __init__(self) -> None:
        pass
    def bubble(myList):
        # function for bubble search
        # simply swaps adjacent values if they're ordered wrong
        lengthList = len(myList)
        for position2 in range(0,lengthList-1):
            for position in range(0, lengthList-1-position2):
                if myList[position] > myList[position + 1]:
                    myList[position], myList[position + 1] = myList[position + 1], myList[position]
        return myList
    def bogo(myList):
        # randomly sorts lists until correct
        lengthList = len(myList)
        while True:
            # makes a random shuffle of the list
            randomGuess = random.shuffle(myList)
            for iterate in range(0, lengthList-1):
                # checks the order of the list
                if randomGuess[iterate] <= randomGuess[iterate + 1]:
                    # moves onto next value in list
                    pass
                else:
                    # if the guess is wrong order, loop breaks and it guesses again
                    break
            else:
                # if it's correct, it returns the guess
                return randomGuess


class Search():
    pass