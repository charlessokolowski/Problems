"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """


        left, right = 0, len(height) - 1

        leftMax, rightMax = 0, 0

        water = 0

        while left < right:
            #start our left bound if we make sure it is always less than our right then it is going to always be able to have water in it
            if height[left] < height[right]:
                #then we check if our current height is larger than our max height if it is then we can move our max heigh up
                if height[left] >= leftMax:
                    leftMax = height[left]
                #otherwise subtract our max from our curreunt space and add the value to our water
                else:
                    water += leftMax - height[left]
                #either way increase our left by one
                left += 1

            else:
                #if our right current height is larger than our largest we can replace it with our current
                if height[right] >= rightMax:
                    rightMax = height[right]
                #otherwise add the differnce to the water
                else:
                    water += rightMax - height[right]
                #move right to the left
                right -= 1
        #return our water val in the end
        return water
