"""
Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

Example
Example1

Input:
[3,2,2,1,4]
4
Output:
[1,2,2,3,4]
Example2

Input:
[2,1,1,2,2]
2
Output:
[1,1,2,2,2]
"""

import random

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):

        def partition3(colors, left, right):
            #need to set the i to left position since that will be the 0 posiiton for the current list
            pivot, i = colors[left], left

            #hold left and right in values
            less, greater = left, right

            #only while the value of i is less than or equal to the greater will this run
            while i <= greater:
                if colors[i] < pivot:
                    colors[i], colors[less] = colors[less], colors[i]
                    less += 1
                    i += 1
                elif colors[i] > pivot:
                    colors[i], colors[greater] = colors[greater], colors[i]
                    greater -= 1
                else:
                    i += 1

            return less, greater

        def randomPivot(colors, left, right):

            if left >= right:
                return

            pivot = random.randint(left, right)

            colors[pivot], colors[left] = colors[left], colors[pivot]

            less, greater = partition3(colors, left, right)

            randomPivot(colors, left, less - 1)

            randomPivot(colors, greater + 1, right)

        left, right = 0, len(colors) - 1

        randomPivot(colors, left, right)

        return colors
