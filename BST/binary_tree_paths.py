"""
Given a binary tree, return all root-to-leaf paths.

Example
Example 1:

Input：{1,2,3,#,5}
Output：["1->2->5","1->3"]
Explanation：
   1
 /   \
2     3
 \
  5
Example 2:

Input：{1,2}
Output：["1->2"]
Explanation：
   1
 /
2

"""



"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):

        if not root:
            return []

        #check if there are no children if there are not any then it returns the current value as a list by itsel
        if not root.left and not root.right:
            return [str(root.val)]

        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)

        #if there are no more left or right branches for the current node then create a new list
        result = []

        #iterate over the right and left and append each value from the current node to the results list
        for i in left + right:
            result.append(str(root.val) + "->" + i)
            
        return result
