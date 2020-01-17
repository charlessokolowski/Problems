"""
Given a set of distinct integers, return all possible subsets.

Example
Example 1:

Input: [0]
Output:
[
  [],
  [0]
]
Example 2:

Input: [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):

        #has to be sorted to begin with
        nums.sort()

        result = []

        self.dfs(nums, result, 0, [])

        return result


    def dfs(self, nums, result, index, path):
        #dont need base case since we ran the for loop below
        result.append(path[:])


        #iterate over the remainder the recursionlevel
        for i in range(index, len(nums)):
            #basic level for dfs in increment it by one
            path.append(nums[i])
            self.dfs(nums, result, i + 1, path)
            path.pop()
