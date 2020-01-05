"""
Given a big sorted array with non-negative integers sorted by non-decreasing order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).

Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.

Return -1, if the number doesn't exist in the array.

Example
Example 1:

Input: [1, 3, 6, 9, 21, ...], target = 3
Output: 1
Example 2:

Input: [1, 3, 6, 9, 21, ...], target = 4
Output: -1
"""

class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """

    def searchBigSortedArray(self, reader, target):
        #set right and left to 0,1 so right can be multiplied until in range of the target
        left, right = 0, 1
        #increments right until it is greater than the target
        while reader.get(right) < target:
            right *= 2
        while left + 1 < right:
            mid = (left + right) // 2
            #have to check the reader.get method on the mid
            if reader.get(mid) >= target:
                right = mid
            else:
                left = mid
        #checks if either the left or right are the target, left first if neither are return -1
        if reader.get(left) == target:
            return left
        if reader.get(right) == target:
            return right
        else:
            return -1
