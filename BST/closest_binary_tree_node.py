"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Example
Example1

Input: root = {5,4,9,2,#,8,10} and target = 6.124780
Output: 5
Explanation：
Binary tree {5,4,9,2,#,8,10},  denote the following structure:
        5
       / \
     4    9
    /    / \
   2    8  10
Example2

Input: root = {3,2,4,1} and target = 4.142857
Output: 4
Explanation：
Binary tree {3,2,4,1},  denote the following structure:
     3
    / \
  2    4
 /
1

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
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        #start the nodes to the root of the low and high
        low, high = root, root

        while root:
            #check if the nodes val is the target if it is return that
            if root.val == target:
                return root.val
            #if the nodes val is greater than the target than we set the low node the left node otherwise set it to the right and move the root that same way
            elif root.val > target:
                low = root
                root = root.left
            else:
                high = root
                root = root.right
        #checks the val of each and returns the one that is closest to the target and returns it
        if abs(low.val - target) < abs(high.val - target):
            return low.val
        else:
            return high.val
