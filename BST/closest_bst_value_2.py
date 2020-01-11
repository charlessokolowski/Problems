"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Example
Example 1:

Input:
{1}
0.000000
1
Output:
[1]
Explanation：
Binary tree {1},  denote the following structure:
 1
Example 2:

Input:
{3,1,4,#,2}
0.275000
2
Output:
[1,2]
Explanation：
Binary tree {3,1,4,#,2},  denote the following structure:
  3
 /  \
1    4
 \
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
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):

        nodeList = []

        result = []

        #use a function recursively to add to node vals to the nodelist using in order
        def recurse(root):
            if not root:
                return


            recurse(root.left)
            nodeList.append(root.val)
            recurse(root.right)

        recurse(root)

        #use binary search to find the k elements refer to k closest in binary search folder
        def helper(nodeList, target):

            left, right = 0, len(nodeList) - 1

            while left + 1 < right:

                mid = (left + right) // 2

                if nodeList[mid] < target:
                    left = mid

                else:
                    right = mid

            if target <= nodeList[left]:
                return left

            return right

        def expand(left, right, nodeList):

            if left < 0:
                return False
            if right > len(nodeList) - 1:
                return True

            return target - nodeList[left] <= nodeList[right] - target

        right = helper(nodeList, target)
        left = right - 1

        for _ in range(k):
            if expand(left, right, nodeList):
                result.append(nodeList[left])
                left -= 1
            else:
                result.append(nodeList[right])
                right += 1

        return result
