"""
Given a list of numbers, return all possible permutations.

Example
Example 1:

Input: [1]
Output:
[
  [1]
]
Example 2:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):

        result, path = [], []

        self.dfs(nums, result, path)

        return result

    def dfs(self, nums, result, path):

        #base case is when we have no elements left in the nums since we are slicing it using the range function below
        if not nums:
            result.append(path[:])


        for i in range(len(nums)):

            #pass back a modified version of our nums list to the next level of recursion to handle the remainder of the list so we concadinate everything before the i to everything after the i
            path.append(nums[i])
            self.dfs(nums[ : i] + nums[i + 1:], result, path)
            path.pop()
