"""
Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top.

Example
Example 1:

Input: nums = [1, 2, 4, 8, 6, 3]
Output: 8
Example 2:

Input: nums = [10, 9, 8, 7],
Output: 10
Notice
Arrays are strictly incremented, strictly decreasing
"""



class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        #create left and right pointers
        left, right = 0, len(nums) - 1
        #most important part of algorithm
        while left + 1 < right:
            #create mid using left left and right
            mid = (left + right) // 2
            #checks if the right side of mid is increasing if it is then left can be mid else set right to mid
            if nums[mid] < nums[mid + 1]:
                left = mid
            else:
                right = mid
            #return the max of the two
        return max(nums[left],nums[right])
