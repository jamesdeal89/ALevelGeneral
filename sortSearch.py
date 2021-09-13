# sorting and searching functions

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


class Search():
    pass