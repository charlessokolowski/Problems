"""
Suppose a sorted array in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

Example
Example 1:

Input：[4, 5, 6, 7, 0, 1, 2]
Output：0
Explanation：
The minimum value in an array is 0.
Example 2:

Input：[2,1]
Output：1
Explanation：
The minimum value in an array is 1.
"""

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            #compare right with mid so that it is always going to look at the end of the list first and compore vals
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid

        return min(nums[left], nums[right])
