"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).


The function prototype should be:

bool isMatch(string s, string p)

isMatch("aa","a") → false

isMatch("aa","aa") → true

isMatch("aaa","aa") → false

isMatch("aa", "a*") → true

isMatch("aa", ".*") → true

isMatch("ab", ".*") → true

isMatch("aab", "c*a*b") → true

Example
Example 1:

Input："aa"，"a"
Output：false
Explanation：
unable to match
Example 2:

Input："aa"，"a*"
Output：true
Explanation：
'*' can repeat a
"""

class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):


        lengS = len(s)

        lengP = len(p)


        dp = [[False for _ in range(lengP + 1)] for _ in range(lengS + 1)]

        dp[0][0] = True

        for i in range(2, lengP + 1):

            #the only way that the top row will have a True is if it has * since it can erase one position, so it needs to have * in string for any value to be True
            if p[i -1] == "*" and dp[0][i - 2] == True:
                dp[0][i] = True


        for i in range(1, lengS + 1):
            for j in range(1, lengP + 1):
                #for all cases that arent * if the diagonal is True and the strings are either the same or it is a "." set the value to true
                if p[j-1] != "*":
                    dp[i][j] = dp[i -1][j - 1] and (s[i -1] == p[j - 1] or p[j - 1] == ".")
                else:
                    #if either the 2 to the left are true or the direct left then the current node is true
                    dp[i][j] = dp[i][j - 2] or dp[i][j -1]

                    #if the pattern before this current pattern equals the current string or its a "." and the above space is True set it to True
                    if (p[j - 2] == s[i -1] or p[j -2] == ".") and dp[i - 1][j]:
                        dp[i][j] = True

        return dp[-1][-1]
