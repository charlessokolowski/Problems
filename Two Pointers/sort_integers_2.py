"""
Given an integer array, sort it in ascending order in place. Use quick sort, merge sort, heap sort or any O(nlogn) algorithm.

Example
Example1:

Input: [3, 2, 1, 4, 5],
Output: [1, 2, 3, 4, 5].
Example2:

Input: [2, 3, 1],
Output: [1, 2, 3].
"""

import random

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):

        left, right = 0, len(A) -1
        #firt sub function it takes the left and right and returns the pivot index for the current element, and replaces the element to that position
        def partition(l, r):
            #set a border variable and a pivot variable which will be used to check the elements
            border = l
            pivot = A[l]

            #need to iterate over l +1 and right +1
            for i in range(l + 1, r + 1):
                #if the current item is less than or equal to the pivot set it to the pivot and swap them
                if A[i] <= pivot:
                    border += 1
                    A[i], A[border] = A[border], A[i]
            #once the correct postion is found set it to that position
            A[l] , A[border] = A[border], A[l]
            return border

        def randomPivot(l, r):
            #base case
            if l >= r:
                return

            #generates an int in the range of the new list
            pivot = random.randint(l, r)

            #replce that pivot and left
            A[pivot] , A[l] = A[l], A[pivot]

            #call our partition function and hold the returned border
            pivotPosition = partition(l, r)

            #calls recursion on left
            randomPivot(l, pivotPosition - 1)

            #calls recursion on right
            randomPivot(pivotPosition + 1, r)


        randomPivot(left, right)



"""
merge sort
"""

"""

import random

class Solution:
    """
    """
    @param A: an integer array
    @return: nothing
    """
    """

    def sortIntegers2(self, A):
        #base case
        if len(A) <= 1:
            return

        #seperate the list by taking the mid index and setting that to the left and right
        mid = len(A) // 2

        left, right = A[ :mid], A[mid: ]

        #calls function recursively on the left and right list, will only stop when the left and right lists are 1 item
        self.sortIntegers2(left)

        self.sortIntegers2(right)

        #need 3 placeholders
        i, j, m = 0, 0, 0

        #left placeholder is i and right is j, and i iterates through the left list and right iterates throught the right list
        while i < len(left) and j < len(right):

            #if the current index in the left list is less than the current right then set the value of our main list to that and increment i otherwise add the right and increase j, after they re all down increment the m by 1
            if left[i] < right[j]:
                A[m] = left[i]
                i += 1
            else:
                A[m] = right[j]
                j += 1
            m += 1

        the remainder of the elements from the left or right will be handled below
        while i < len(left):
            A[m] = left[i]
            i += 1
            m += 1

        while j < len(right):
            A[m] = right[j]
            j += 1
            m += 1


"""
