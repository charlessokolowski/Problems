"""
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
Return null if LCA does not exist.

Example
Example1

Input:
{4, 3, 7, #, #, 5, 6}
3 5
5 6
6 7
5 8
Output:
4
7
7
null
Explanation:
  4
 / \
3   7
   / \
  5   6

LCA(3, 5) = 4
LCA(5, 6) = 7
LCA(6, 7) = 7
LCA(5, 8) = null

Example2

Input:
{1}
1 1
Output:
1
Explanation:
The tree is just a node, whose value is 1.
"""


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):


        def recurse(root, A, B):


            #base case returns False, False, and none. the first 2 are booleans that will be replaced later and the second will hold the value of the node
            if not root:
                return False, False, None

            #this sets variables of the output of the recursion. when this is called it will return 2 booleans and a node.
            left_a, left_b, left_node = recurse(root.left, A, B)
            right_a, right_b, right_node = recurse(root.right, A, B)

            #if any of the below conditions are true then the whole of either a or b will be true
            a = left_a or right_a or root == A
            b = left_b or right_b or root == B

            #checls the root as soon as the a and be are checked, if the root is either A or b then return the a or b and the current node
            if root == A or root == B:
                return a, b, root

            #if both the left and the right node have values then return the current root along with the booleans for a and b
            if left_node and right_node:
                return a, b, root

            #if only the left node if viable then it only passes the left node up the recursion as well as the below
            if left_node:
                return a, b, left_node

            if right_node:
                return a, b, right_node

            #in the event that the node has neither a left and right return the a and b with a none node
            return a, b, None

        #unpack the recursion and compare the booleans from it, if they are both the same then the node is called else return a none type node
        a, b , lca = recurse(root, A, B)
        if a == b:
            return lca
        else:
            return None
