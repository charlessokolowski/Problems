"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Example
Example 1:

Input: [0]
Output:
[
  [],
  [0]
]
Example 2:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]



#in the first round the index will be 0 result will be [] and when it reaches maximum recursion depth it will be 1,2,2 and the result will be [[], [1], [2], [1, 2], [1, 2, 2]] then it backs out to the level where ther efirst 2 is and repeats 2 is in the list and do it skips that then continues until it is 2,2
"""

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):

        nums.sort()

        result = []

        self.dfs(nums, result, 0, [])

        return result


    def dfs(self, nums, result, index, path):

        #immediately append thiongs to the result list
        result.append(path[:])


        #iterate over the remainder from each level of recuresion
        for i in range(index, len(nums)):
            #checks if we are at the previosu recrusion level if it is and the current val is the same as the previous then go to next loop
            if i > index and nums[i] == nums[i -1]:
                continue
            #append the current i to path and recursion on the next index
            path.append(nums[i])
            self.dfs(nums, result, i + 1, path)
            #once the recursion ends pop the last item
            path.pop()
