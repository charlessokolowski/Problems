"""
Given some points and an origin point in two-dimensional space, find k points which are nearest to the origin.
Return these points sorted by distance, if they are same in distance, sorted by the x-axis, and if they are same in the x-axis, sorted by y-axis.

Example
Example 1:

Input: points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
Output: [[1,1],[2,5],[4,4]]
Example 2:

Input: points = [[0,0],[0,9]], origin = [3, 1], k = 1
Output: [[0,0]]

#heap essentially turns youre designated item into a stack or a queue.
"""

import heapq

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):

        distMap =[]

        result = []


        #iterate over the points list and for each point pass it into the distance formula
        for point in points:

            #the distance formula uses euclydian distance and spits it back to use as a value
            distance = self.findDistance(point, origin, distMap)
            #push it using a heapq using our distmap list, add the values in negative so they can be added as the lowest since by default heaps store lowest values first
            heapq.heappush(distMap, (-distance, -point.x, -point.y))
            #if the distnace map every gets made larger then our k by using this heap we pop the top aka the lowest value or our highest value
            if len(distMap) > k:
                heapq.heappop(distMap)

        #treat the map like a queue
        while len(distMap) > 0:
            #unpack the popped val from heap the diff is usless so we kist keep the x and y  then append it to the results as the point
            dist, x, y = heapq.heappop(distMap)
            result.append([-x, -y])

        #since we put our results in negative we need to reverse the list
        return result[:: -1]


    def findDistance(self, point, origin, distMap):
        
        return ((origin.x - point.x) ** 2 + (origin.y - point.y) ** 2) ** (1/2)
