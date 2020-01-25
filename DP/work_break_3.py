"""
Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by inserting whitespaces to the sentence so that each word can be found in the dictionary.

Example
Example1

Input:
"CatMat"
["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
Output: 3
Explanation:
we can form 3 sentences, as follows:
"CatMat" = "Cat" + "Mat"
"CatMat" = "Ca" + "tM" + "at"
"CatMat" = "C" + "at" + "Mat"
Example1

Input:
"a"
[]
Output: 0

"""

class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):

        n = len(s)

        #make a grid of size length of the list by the length of the list
        dp = [[0] * n for _ in range(n)]

        s = s.lower()

        lowerSet = set()

        #iterate over the dictionary and convert them all to lower and change it to a set
        for i in dict:
            lowerSet.add(i.lower())

        #iterate over the dp grid and if the slices of the string are in our set then replace the current positon on our grid with a 1
        for i in range(n):
            for j in range(i, n):
                if s[i: j + 1] in lowerSet:
                    dp[i][j] = 1

        #check each possible combination of each iteration the current i j positions values cooinceide with i k and k+1 and j each time if both values are 1 then add it to the current i j
        for i in range(1):
            for j in range(i, n):
                for k in range(i, j):
                    dp[i][j] += dp[i][k] * dp[k + 1][j]

        #return our last position in the top of our grid
        return dp[0][-1]
