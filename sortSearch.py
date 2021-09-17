# sorting and searching functions
import random

class Sort():
    """ a sorting class containing sorting for bubble, merge, heap and quick """
    def __init__(self):
        pass
    def bubble(self, myList):
        """ function for bubble search. simply swaps adjacent values if they're ordered wrong """
        lengthList = len(myList)
        # loops for each value in list
        for position2 in range(0,lengthList-1):
            # loops through each position for the list
            for position in range(0, lengthList-1-position2):
                # checks if the position value is greater than the next position value
                if myList[position] >= myList[position + 1]:
                    # if they are, they are swapped.
                    myList[position], myList[position + 1] = myList[position + 1], myList[position]
        return myList
    def bogo(self, myList):
        """randomly sorts lists until correct"""
        lengthList = len(myList)
        while True:
            # makes a random shuffle of the list
            random.shuffle(myList)
            for iterate in range(0, lengthList-1):
                # checks the order of the list
                if myList[iterate] <= myList[iterate + 1]:
                    # moves onto next value in list
                    pass
                else:
                    # if the guess is wrong order, loop breaks and it guesses again
                    break
            else:
                # if it's correct, it returns the guess
                return myList
        
    def selection(self, myList):
        """goes up from first values and compares it to ever other value, if one is bigger, they're swapped"""
        for iterate in range(len(myList)):
            # saves position of smallest value: default is first value.
            smallest = iterate
            # moves onto next value in list for each loop
            for position in range(iterate + 1, len(myList)):
                # checks if the current position is largest and loops for every other position.
                if myList[smallest] > myList[position]:
                    # swaps the saved 'smallest position' with the current position if it's smaller.
                    smallest = position
            # swaps the value of the smallest value found with the current value.
            myList[smallest], myList[iterate] = myList[iterate], myList[smallest]
        # return the ordered list
        return myList
        


class Search():
    def binary(self, myList, search):
        """a search method that uses midpoints and determine the location of a value and splits the list to narrow it down."""
        # start values for limits are the entire list.
        start = 0
        end = len(myList)
        while True:
            # middle is put at the middle of the whole list at the start
            middlePos = (start + end)//2
            # if the value we want is less than the middle, we disregard the top half of the list
            if search < myList[middlePos]:
                end = middlePos
            # if the value we want is more than the middle, we disregard the bottom half of the list
            if search > myList[middlePos]:
                start = middlePos
            # if the value we want is the middle, we exit the loop and return the position
            if search == myList[middlePos]:
                positionFound = middlePos
                break
        return positionFound
    
    def linear(self, myList, search):
        """a search method that simply iterates through the list checking each value against a search one by one."""
        counter = 0
        for element in myList:
            if element == search:
                return counter
            else:
                counter += 1
        
