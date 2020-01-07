"""
Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.

Example
Example 1:

Input:{1,2,5,3,4,#,6}
Output：{1,#,2,#,3,#,4,#,5,#,6}
Explanation：
     1
    / \
   2   5
  / \   \
 3   4   6

1
\
 2
  \
   3
    \
     4
      \
       5
        \
         6
Example 2:

Input:{1}
Output:{1}
Explanation：
         1
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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):

        if not root:
            return root

        nodeList = []

        #fills the nodeList with the nodes from the root
        def recurse(root):
            if not root:
                return
            nodeList.append(root)

            recurse(root.left)
            recurse(root.right)

        recurse(root)

        #grabs the root from the nodes list and pops it so it just has the other nodes in it
        c = nodeList[0]
        nodeList.pop(0)

        #while the list is no empty assign the left to none and the right to the next value from the list then set the node to the right
        while nodeList:
            c.left = None
            d = nodeList.pop(0)
            c.right = d
            c = c.right

        return root
