"""
Given a set of candidtate numbers candidates and a target number target. Find all unique combinations in candidates where the numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Example
Example 1:

Input: candidates = [2, 3, 6, 7], target = 7
Output: [[7], [2, 2, 3]]
Example 2:

Input: candidates = [1], target = 3
Output: [[1, 1, 1]]
"""


class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):


        candidates = sorted(list(set(candidates)))
        result = []
        self.dfs(candidates, target, result, 0, [])
        return result

    #2 base cases, if the current target value is less than 0 return, so it goes back to previous recursion depth or if it does == 0 append the current path
    def dfs(self, candidates, target, result, index, path):

        if target < 0:
            return
        if target == 0:
            result.append(path[:])
            return
        #iterate over the current i to the end of the list
        for i in range(index, len(candidates)):
            #append the current i to the path
            path.append(candidates[i])
            #recursively call the function modidying i and the target, the target get subtracted from our current target and the current index
            self.dfs(candidates, target - candidates[i], result, i, path)
            path.pop()
