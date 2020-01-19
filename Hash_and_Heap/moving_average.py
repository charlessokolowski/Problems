"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example
Example 1:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1 // return 1.00000
m.next(10) = (1 + 10) / 2 // return 5.50000
m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
m.next(5) = (10 + 3 + 5) / 3 // return 6.00000
"""

from collections import deque

class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        self.size = size
        self.nextStart = deque([])
        self.total = 0
        self.count = 0
    """
    @param: val: An integer
    @return:
    """
    def next(self, val):

        #add all vals to the total and the queue
        self.total += val

        self.nextStart.append(val)


        #use a count to track if we are at the size, if we are the the size given then we pop the left most element and subtract the queue
        if self.count == self.size:
            self.total -= self.nextStart.popleft()
        else:
            #otherwise we just increment the count
            self.count += 1

        #can return total divided by the count outside of all if statements
        return self.total / self.count

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)
