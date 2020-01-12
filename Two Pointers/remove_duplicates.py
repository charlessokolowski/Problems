"""
Given an array of integers, remove the duplicate numbers in it.

You should:

1) Do it in place in the array.
2) Move the unique numbers to the front of the array.
3) Return the total number of the unique numbers.
Example
Example 1:

Input:
nums = [1,3,1,4,4,2]
Output:
[1,3,4,2,?,?]
4
Explanation:

1) Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
2) Return the number of unique integers in nums => 4.
Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.
Example 2:

Input:
nums = [1,2,3]
Output:
[1,2,3]
3

"""
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):

        left, right = 0, 0

        #need to create visited set so we can compare the elements
        visited, duplicates = set(), []


        #start moving the right pointer
        while right < len(nums):
            #if the current element at the right pointer is not in the visited set then add it to the visited set
            if nums[right] not in visited:
                visited.add(nums[right])
                #checks if numbers arent the same. if they are the same do nothing and increase the left pointer to one more, otherwise set the left to th the right pointers element and then increment the left
                if nums[left] != nums[right]:
                    nums[left] = nums[right]
                left += 1
            else:
                #if its in the visited set just append it to the duplicate list
                duplicates.append(nums[right])

            #after the rest of the codes executes increment the right side by one
            right += 1

        #since out left pointer is already set at the elements that arrent replaced we can add a placeholder for that variable to return at the end
        position = left

        #while the left pointer isnt at the end of the list iterate over the duplicate list and check each left eleemnt one at a time with the current element and then increment the left
        while left < len(nums):
            for i in duplicates:
                nums[left] = i
                left += 1

        return position
