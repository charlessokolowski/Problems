"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Test case Input:
11110
11010
11000
00000

Output: 1

"""


from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        queue = deque([])
        count = 0
        visited = set()
        #need to declare directions to iterate through later
        directions = [(-1, 0),(1, 0),(0, 1),(0, -1)]

        #sub function that does BFS for you
        def bfs(row,col):
            #immediately puts the popped value into visited
            queue.append((row, col))
            visited.add((row, col))
            while queue:
                curRow,curCol = queue.popleft()
                #iterate over each set of values for directions
                for x,y in directions:
                    newRow,newCol = curRow + x, curCol + y
                    #make sure to check if in range first or will get index out of range
                    if (newRow, newCol) not in visited and 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]) and grid[newRow][newCol] == "1":
                        visited.add((newRow, newCol))
                        queue.append((newRow, newCol))


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                #increment count only when your bfs is done also make sure that 1 is a string
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    count +=1
        return count
