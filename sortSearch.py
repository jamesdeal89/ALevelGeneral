# sorting and searching functions

class Sort():
    # a sorting class containing sorting for bubble, merge, heap and quick
    def __init__(self) -> None:
        pass
    def bubble(self, myList):
        # function for bubble search
        # simply swaps adjacent values if they're ordered wrong
        lengthList = len(myList)
        for position in range(0, lengthList):
            if myList[position] > myList[position + 1]:
                myList[position], myList[position + 1] = myList[position + 1], myList[position]
        return myList


class Search():
    pass