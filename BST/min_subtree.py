"""
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

Example
Example 1:

Input:
{1,-5,2,1,2,-4,-5}
Output:1
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
1   2 -4  -5
The sum of whole tree is minimum, so return the root.
Example 2:

Input:
{1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.
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
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    #create global variables in python using init
    def __init__(self):
       self.minTree = float("inf")
       self.lowestNode = None


    def findSubtree(self, root):

        if not root:
            return 0

        #recursive funtion calls the funtion on the left then right an each time checks the val
        #######################################################
        def recurse(root):
            if not root:
                return 0

            left = recurse(root.left)
            right = recurse(root.right)
            total = left + right + root.val

            #if the total is less than the current total then set it to that as well as the current node
            if total < self.minTree:
                self.minTree = total
                self.lowestNode = root

            return total

        ########################################################

        #calls the recurse function with the root
        recurse(root)

        #returns the node that from our global variable
        return self.lowestNode
