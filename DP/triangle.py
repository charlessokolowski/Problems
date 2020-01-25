"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

Example
Example 1:

Input the following triangle:
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
Output: 11
Explanation: The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Example 2:

Input the following triangle:
[
     [2],
    [3,2],
   [6,5,7],
  [4,4,8,1]
]
Output: 12
Explanation: The minimum path sum from top to bottom is 12 (i.e., 2 + 2 + 7 + 1 = 12).

"""

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):

        n = len(triangle)

        #create our grid populationg each layer with 1 more element so our grid will be the same as our triangle
        dp = [[0] * (i + 1) for i in range(n)]

        #set the root to the triangle head
        dp[0][0] = triangle[0][0]

        #first populate the lefthand side and the diagonal lines of the triangle
        for i in range(1, n):
            #this populates the left hand side, uses the previous grid value and the value from the triangle in this position
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            #this populates the diagonal line, uses columns value to create the diagonal position in our grid and uses the previous diagonal plus that same value from our triangle
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]



        #this fills the blanks iterate over 2 to n since our previous for loop already populates 0 and 1
        for i in range(2, n):
            #since we only populated left hand side we can itarate from 1 til i since our current i will still be the diagonal line
            for j in range(1, i):
                #checks the value of the position directly above us and the poisiton to the left of that and then use the value from the triangle of the current i and j
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]


        #return the min of the last element in our grid
        return min(dp[n-1])
