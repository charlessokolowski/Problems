"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example
Example 1:

Input: nums = [0, 1, 0, 3, 12],
Output: [1, 3, 12, 0, 0].
Example 2:

Input: nums = [0, 0, 0, 3, 1],
Output: [3, 1, 0, 0, 0].
"""

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):

        #start both left and right to 0
        left, right = 0, 0

        #iterate with the right variable through the nums list
        while right < len(nums):
            #if the current right isnt 0 and the current left isnt the current right then replace the current left with the current right then increment both the life and right when that loop ends
            if nums[right] != 0:
                if nums[left] != nums[right]:
                    nums[left] = nums[right]
                left += 1
            right += 1


        #after the above code exits the left pointer will be the remainder of the codes that havent been moved. meaning that the remainder of the code can be replaced with 0 by iterating through the left and for each left seeting tha balue to 0
        while left < len(nums):
            nums[left] = 0
            left += 1
