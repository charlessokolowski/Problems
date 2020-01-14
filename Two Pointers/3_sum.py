"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Example
Example 1:

Input:[2,7,11,15]
Output:[]
Example 2:

Input:[-1,0,1,2,-1,-4]
Output:	[[-1, 0, 1],[-1, -1, 2]]
"""

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):

        #sort the list first so you can traverse each element by lowest to highest
        numbers.sort()

        result = []

        # iterate over the list
        for i in range(len(numbers)):

            #set the left equal to one more than the current i so it can iterate over the rest of them
            left, right = i + 1 , len(numbers) - 1

            #if the current i is the same as the previous i then the function skips it
            if numbers[i] > 0 and numbers[i] == numbers[i - 1]:
                continue


            while left < right:
                #if the combined numbers are greater move right, if less move left otherwise append the current set to the results, and skip and remaining duplicates in the left and right to complete the rest of the sets unitl you get another left and ribght that is unique or the code ends
                if numbers[i] + numbers[left] + numbers[right] > 0:
                    right -= 1
                elif numbers[i] + numbers[left] + numbers[right] < 0:
                    left += 1
                else:
                    if [numbers[i], numbers[left], numbers[right]] not in result:
                        result.append([numbers[i], numbers[left], numbers[right]])
                        while left < right and numbers[left] == numbers[left + 1]:
                            left += 1
                        while left < right and numbers[right] == numbers[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    else:
                        left += 1
                        right -= 1

        return result
