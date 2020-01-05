"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"

"""


from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        serial = []

        queue = deque([root])

        #use a queue to iterate through the nodes if the val is none then add # to string else add the val to the string and add the left and right of that node to  the queue
        while queue:
            node = queue.popleft()
            if not node:
                serial.append("#")
            else:
                serial.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        #converts the list to a string
        return " ".join(serial)





    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return

        nodes = []
        #split the list by spaces
        for i in data.split():
            #must either turn to a node straight away or None
            if i == "#":
                nodes.append(None)
            else:
                nodes.append(TreeNode(i))
        #start a parentList with only the first parent as the first item
        parentList = [nodes[0]]
        #create indexes to iterate over our nodes List
        parent, child = 0, 1
        #needs to be less than parentList because each time we finish while loop it will append new parent to list if possible
        while parent < len(parentList):
            #creates new variable with each index of the parent
            newParent = parentList[parent]
            parent += 1
            #assigns the right and left values using the child index and the nodes List
            newParent.left = nodes[child]
            newParent.right = nodes[child + 1]
            #increment the child by 2 since we used 2 indexes to find parents children
            child += 2
            #checks to see if the values is valid and if it is adds it to the parentList left first
            if newParent.left:
                parentList.append(newParent.left)
            if newParent.right:
                parentList.append(newParent.right)
        #returns the first item in the parentList which is a node connecting all the other nodes
        return parentList[0]



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
