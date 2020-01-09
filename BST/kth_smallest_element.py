"""
902. Kth Smallest Element in a BST
中文English
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Example
Example 1:

Input：{1,#,2},2
Output：2
Explanation：
	1
	 \
	  2
The second smallest element is 2.
Example 2:

Input：{2,1,3},1
Output：1
Explanation：
  2
 / \
1   3
The first smallest element is 1.
"""

"""
Given k = 7

        5
        /\
      4   8
    /    /  \
   2    7    10
/   \  /
1   3  6

1) node = 0 -> 5
stack = [5, 4, 2, 1]
2) node = 1
stack = [5, 4 ,2]
3) node = 2 -> 3
stack = [5, 4]
4) node = 3
stack = [5,4]
5) node = 4
stack = [5]
6) node = 5 -> 8
stack = [8, 7, 6]
7) node = 6
stack = [8,7]

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
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):

        #set up a dummy node that just stores random garbage so that we can return back to the root
        dummy = TreeNode(0)
        #set the right side of out dummy to the root
        dummy.right = root
        #create a stack with the dummy
        stack = [dummy]

        for _ in range(k):
            node = stack.pop()
            #sets the node to the right if there is not a current right it doesnt pass the next while loop
            node = node.right

            while node:
                #if the node is valid you append it to the stack and set it to the left node which  will then be checked in the next round of the while loop
                stack.append(node)
                node = node.left
            if not stack:
                return None
        #outside of the for loop return the last item in the stack which will always be the last item that we didnt pop from the stack
        return stack[-1].val
