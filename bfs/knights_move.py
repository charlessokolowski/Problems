"""

Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.
Return -1 if destination cannot be reached.

Example
Example 1:

Input:
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2]
Output: 2
Explanation:
[2,0]->[0,1]->[2,2]

"""





from collections import deque

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """
    def shortestPath(self, grid, source, destination):
        #create the directions list using the given commands. think knight moves in chess
        directions = [(1, 2), (1,-2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

        movesMap = {}

        #unpack the x and y
        x,y = source.x, source.y

        #add the soruce to the map with 0 value and the queue
        movesMap[(x,y)] = 0

        queue = deque ([(x,y)])

        while queue:
            c,d = queue.popleft()
            #check to see if the current val is the destination, if it is can return the value
            if (c,d) == (destination.x, destination.y):
                return movesMap[(c,d)]
            #iterate over the directions and create each new move
            for dirX, dirY in directions:
                newX, newY = c + dirX, d + dirY
                #check to make sure each new coord is in the map and if the new space is passable and then add the new value to the map as well as the queue
                if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]) and (newX, newY) not in movesMap and not grid[newX][newY]:
                    movesMap[(newX, newY)] = movesMap[(c,d)] + 1
                    queue.append((newX, newY))
        #if the while loop ends without it ever returning the value it is not possible so return -1
        return -1
