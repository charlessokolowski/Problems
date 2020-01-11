"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example
Example 1:

add(1); add(3); add(5);
find(4) // return true
find(7) // return false
"""

class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    #using lists and binary search like approach
    def __init__(self):
        self.numberHolder = []

    def add(self, number):
        self.numberHolder.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        #have to sort the list so youre always comparing highest and lowest values
        self.numberHolder.sort()

        left, right = 0, len(self.numberHolder) - 1

        while left < right:


            #if the combined values are lower add one to the left, if its higher subtract one from the right and if its the value return true
            if self.numberHolder[left] + self.numberHolder[right] < value:
                left  += 1

            elif self.numberHolder[left] + self.numberHolder[right] > value:
                right -= 1

            else:
                return True

        return False



class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.numberHolder ={}

    #creates a dictionary with counts of each number
    def add(self, number):
        if number not in self.numberHolder:
            self.numberHolder[number] = 1
        else:
            self.numberHolder[number] += 1
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):

        #iterate through our dic
        for i in self.numberHolder:
            #sets our new value to each index minus the target
            check = value - i

            #if the target count at the current position or the current i isnt included in our calculations AND its in our list return true otherwise it is not in our dict and it is not possible
            if (self.numberHolder[i] > 1 or value - i != i) and check in self.numberHolder:
                return True
        return False
