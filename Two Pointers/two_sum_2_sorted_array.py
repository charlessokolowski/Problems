"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

Example
Example 1:

Input: nums = [2, 7, 11, 15], target = 9
Output: [1, 2]
Example 2:

Input: nums = [2,3], target = 5
Output: [1, 2]
"""

class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        #two pointers starting at left index and right index
        left, right = 0, len(nums) -1
        #if the left and right dont meet
        while left < right:

            #if the left position and the right positions value is greater than add 1 to the left else if its less add one to the left otherwise you have the values since it == target
            if nums[left] + nums[right] > target:
                right -= 1

            elif nums[left] + nums[right] < target:
                left += 1

            else:
                return [left +1, right +1]
