"""
Given an array num and a number target. Find all unique combinations in num where the numbers sum to target.

Example
Example 1:

Input: num = [7,1,2,5,1,6,10], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
Example 2:

Input: num = [1,1,1], target = 2
Output: [[1,1]]
Explanation: The solution set must not contain duplicate combinations.
"""
class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        num.sort()

        result = []

        self.dfs(num, target, result, 0, [])
        return result

    def dfs(self, num, target, result, index, path):


        if target < 0:
            return
        if target == 0:
            if path not in result:
                #append a deep copy of the code
                result.append(path[:])
                return
            else:
                return

        #iterate over the current i to the len of the list
        for i in range(index, len(num)):
            #add the current i to our path and then increase the i to one to check the next index
            path.append(num[i])
            self.dfs(num, target - num[i], result, i + 1, path)
            path.pop()
