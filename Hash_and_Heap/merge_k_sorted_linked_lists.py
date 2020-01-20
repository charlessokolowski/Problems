"""
Merge k sorted linked lists and return it as one sorted list.

Analyze and describe its complexity.

Example
Example 1:
	Input:   [2->4->null,null,-1->null]
	Output:  -1->2->4->null

Example 2:
	Input: [2->6->null,5->null,7->null]
	Output:  2->5->6->7->null
"""

import heapq


"""
using a heap


Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):

        heap = []

        #iterate over each linked list item and use a while loop to iterate over linked list items
        for list in lists:
            #while the list is not null push each item to the heap and go to next node
            while list:
                heapq.heappush(heap, list.val)
                list = list.next


        #node is a placeholder, and sentinal points to the node so we can change to node and hold all values of the node
        node = ListNode(0)
        sent = node

        #while the heap still has items our next node points to the next item in the heap and add it to our node
        while heap:
            #then set it equal to the node
            node.next = ListNode(heapq.heappop(heap))
            node = node.next
        #point to the nodes next val since started the node as a placeholder
        return sent.next


"""
import heapq
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
"""
class Solution:
    """
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    """
    def mergeKLists(self, lists):

        start, end = 0, len(lists) - 1

        return self.merge(lists, start, end)

    def merge(self, lists, start, end):

        if start == end:
            return lists[start]

        mid = (start + end) // 2

        left = self.merge(lists, start, mid)
        right = self.merge(lists, mid +1, end)

        return self.merge2Lists(lists, left, right)

    def merge2Lists(self, lists, left, right):
        tail = sent = ListNode(0)

        while left and right:
            if left.val > right.val:
                tail.next = right
                right = right.next
            else:
                tail.next = left
                left = left.next
            tail = tail.next

        if left:
            tail.next = left

        if right:
            tail.next = right

        return sent.next

    """
