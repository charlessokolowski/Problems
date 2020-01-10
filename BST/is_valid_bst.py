"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A single node tree is a BST
Example
Example 1:

Input:  {-1}
Output：true
Explanation：
For the following binary tree（only one node）:
	      -1
This is a binary search tree.
Example 2:

Input:  {2,1,4,#,#,3,5}
Output: true
For the following binary tree:
	  2
	 / \
	1   4
	   / \
	  3   5
This is a binary search tree.

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
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):

        def helper(root):
            #base case returns True since we are basically checking until it is false then set the rest to false anyways, and none none
            if not root:
                return True, None, None
            #for each node it has a lmin and max and rmin and max for each child and wether it is true or false
            lIsBst, lMin, lMax = helper(root.left)
            rIsBst, rMin, rMax = helper(root.right)

            #if one of the true values is ever false just pass false along to the rest
            if not lIsBst or not rIsBst:
                return False, None, None
            #if ever the max of the left is greater than the root it invalidates the tree thus return False
            if lMax and lMax >= root.val:
                return False, None, None
            #if ever the right min is greater than the root return false
            if rMin and rMin <= root.val:
                return False, None, None

            #if the nodes have a current lmin or rmax it does nothing else set it to root
            minNode = lMin if lMin else root.val
            maxMode = rMax if rMax else root.val

            #if they all pass as true return true and the max and min nodes for that node
            return True, minNode, maxMode

        #unpacks the recursion and checks the boolean we eastablished and returns that
        isBst, min, max = helper(root)
        return isBst
