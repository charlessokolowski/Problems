"""
Implement a stack by two queues. The queue is first in first out (FIFO). That means you can not directly pop the last element in a queue.

Example
Example 1:

Input:
push(1)
pop()
push(2)
isEmpty() // return false
top() // return 2
pop()
isEmpty() // return true
Example 2:

Input:
isEmpty()
"""

from collections import deque

class Stack:

    #create 2 global queues
    def __init__(self):
        self.queue1 = deque([])
        self.queue2 = deque([])
    """
    @param: x: An integer
    @return: nothing
    """

    #when the push is called remove everything from the first queue left element at a time then put it into the second queue then put the called number into the first queue and replace all the elements in the first queue with the element from the second
    def push(self, x):
        while self.queue1:
            replace = self.queue1.popleft()
            self.queue2.append(replace)
        self.queue1.append(x)
        while self.queue2:
            replace = self.queue2.popleft()
            self.queue1.append(replace)
    """
    @return: nothing
    """
    #just popleft from the main queeu
    def pop(self):
        self.queue1.popleft()
    """
    @return: An integer
    """

    #jsut calls first item of queue
    def top(self):
        return self.queue1[0]

    """
    @return: True if the stack is empty
    """
    #checks boolean if length is less than queue
    def isEmpty(self):
        return len(self.queue1) <= 0
