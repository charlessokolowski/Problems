"""
Find K-th largest element in an array.

Example
Example 1:

Input:
n = 1, nums = [1,3,4,2]
Output:
4
Example 2:

Input:
n = 3, nums = [9,3,2,4,8]
Output:
4

"""
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):

        #to find the k you need to subtract our n from the list so we basically find the differnce or the kth smallest element where k is the remainder of what was left over by n
        left, right, k = 0, len(nums) - 1, len(nums) - n

        #returns the value from the recursion which will be the value at the kth index
        return self.partition(k, nums, left, right)


    def partition(self, k, nums, left, right):


        #base case if ever the left and right are the same return the k since the list cannot be "sorted" anymore
        if left == right:
            return nums[k]


        #set placeholders so we can modify without messing with our iput values
        newLeft, newRight = left, right

        #set the pivot equal to the value, since they pivot index might change and throw our algorithm off
        pivot = nums[(left + right) // 2]


        #need to use our right and left and compare
        while newLeft <= newRight:
            #while the value of the new left is less than the pivot we can skip it so just add one of the new left
            while newLeft <= newRight and nums[newLeft] < pivot:
                newLeft += 1

            #while the value of our right most index is greater than the pivot we can ignore if so increment our index
            while newLeft <= newRight and nums[newRight] > pivot:
                newRight -= 1

            #need to check our indexes again because they might have changed
            if newLeft <= newRight:
                #swap the left with the right and then we can increment both since we know that the left value is higher than our pivot and our right value is less than out pivot
                nums[newLeft], nums[newRight] = nums[newRight], nums[newLeft]
                newLeft += 1
                newRight -= 1

        #check the k against our values from our new right if k is less than our newright then we shrink our list to that index, 0 to new right
        if k <= newRight:
            self.partition(k, nums, left, newRight)

        #check the k again our value of newleft if k i greater than newleft then we shrink our indexed from newleft to the remainder which is the rest of the origianl list
        if k >= newLeft:
            self.partition(k, nums, newLeft, right)


        #k can sometimes fall in between both, in that event just return k
        return nums[k]
