# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        left, right = 0, len(inorder)

        listMap = {values: index for index, values in enumerate(inorder)}

        self.preIndex = 0

        return self.dfs(left, right, preorder, inorder, listMap)

    def dfs(self, left, right, preorder, inorder, listMap):

        if left == right:
            return

        root_val = preorder[self.preIndex]

        root = TreeNode(root_val)

        index = listMap[root_val]

        self.preIndex += 1

        root.left = self.dfs(left, index, preorder, inorder, listMap)

        root.right = self.dfs(index + 1, right, preorder, inorder, listMap)

        return root
        
