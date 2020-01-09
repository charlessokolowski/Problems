"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example
Example  1:
	Input: tree = {1,2,3}
	Output: true

	Explanation:
	This is a balanced binary tree.
		  1
		 / \
		2  3


Example  2:
	Input: tree = {3,9,20,#,#,15,7}
	Output: true

	Explanation:
	This is a balanced binary tree.
		  3
		 / \
		9  20
		  /  \
		 15   7


Example  3:
	Input: tree = {1,#,2,3,4}
	Output: false

	Explanation:
	This is not a balanced tree.
	The height of node 1's right sub-tree is 2 but left sub-tree is 0.
		  1
		   \
		   2
		  /  \
		 3   4
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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):

        def recurse(root):
            #need to return both boolean and number to track both in the recursion
            if not root:
                return True, 0

            #sets the boolean and the left height
            boolie, leftHeight = recurse(root.left)

            #if the boolean for the left height is false return a false and the current left height
            if not boolie:
                return False, leftHeight

            boolie, rightHeight = recurse(root.right)

            if not boolie:
                return False, rightHeight

            #if the height diff is greater than one return false else return true and returns the current subtree height for thr rest of the recursion
            return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1

        #need to unpack the boolean the value is not needed
        result, num = recurse(root)

        return result
