"""
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

Example
Example 1:

Input:
[],9
Output:
0

Example 2:

Input:
[3,2,2,1],2
Output:1
Explanation:
the real array is[1,2,2,3].So return 1
"""

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        if not nums:
            return 0

        left, right = 0, len(nums) - 1

        #set i as iteratator not for loop
        i = left

        less, greater = left, right

        #while the current i is less than our higher index increment
        while i <= greater:
            #if the current position is less than the value swap it with a less value and increment i by one
            if nums[i] < k:
                nums[i], nums[less] = nums[less], nums[i]
                less += 1
                i += 1
            #if the value is greater swap current eleemnt with greater and lower greater
            elif nums[i] > k:
                nums[i], nums[greater] = nums[greater], nums[i]
                greater -= 1
            #if the element is our target do nothing
            else:
                i += 1
        #return our lower bound
        return less



"""
class Solution:
    """
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    """
    def partitionArray(self, nums, k):
        if not nums:
            return 0

        left, right = 0, len(nums) - 1


        while left <= right:
            do while loop to constantly check the current i if it is within the accepted ranges skip the current position otherwise check if the left is less than the right if it is swap the current left and right and increment both
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        #return the left because that will be the index position for the enxt element
        return left

"""
