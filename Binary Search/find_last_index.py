"""
Find the last position of a target number in a sorted array. Return -1 if target does not exist.

Example
Example 1:

Input: nums = [1,2,2,4,5,5], target = 2
Output: 2
Example 2:

Input: nums = [1,2,2,4,5,5], target = 6
Output: -1

"""

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):

        if not nums:
            return - 1
        #create 2 pointers start and end of list
        left, right = 0, len(nums) - 1
        #most important part of binary search needs to check left +1 vs right
        while left + 1 < right:
            #create a mid point
            mid = (left + right) // 2
            #needs to be included since we are looking for the last index.
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        #checks to see right index first if it is return right index else left and if not either return -1
        if nums[right] == target:
            return right
        elif nums[left] == target:
            return left
        else:
            return -1
