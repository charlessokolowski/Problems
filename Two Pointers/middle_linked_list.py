"""
Find the middle node of a linked list.

Example
Example 1:

Input:  1->2->3
Output: 2
Explanation: return the value of the middle node.
Example 2:

Input:  1->2
Output: 1
Explanation: If the length of list is  even return the value of center left one.


"""

"""


Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):

        if not head:
            return None

        #basically start counter at the first and second position
        turtle = head
        rabbit = turtle.next

        #if the rabbit notde and the one after that are valid then advance 1 node for the turtle and 2 for the rabbit
        while rabbit and rabbit.next:
            turtle = turtle.next
            rabbit = rabbit.next.next

        #after the while loop ends just return the turtle 
        return turtle
