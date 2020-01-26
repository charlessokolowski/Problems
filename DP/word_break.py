"""

Given a string s and a dictionary of words dict, determine if s can be broken into a space-separated sequence of one or more dictionary words.

Example
Example 1:
	Input:  "lintcode", ["lint", "code"]
	Output:  true

Example 2:
	Input: "a", ["a"]
	Output:  true

"""

class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):

        if not s:
            return True

        n = len(s)

        #create single row dp n +1 length
        dp = [False] * (n + 1)

        #set first index to true
        dp[0] = True

        #iterate over the string and grab a word from the dict at the same time
        for i in range(1, n + 1):
            for w in dict:
                #if the dp point i - length of the current w is True and the string split which would be i - len(w) to i each one of the words in teh dictionary then set the cyrrent i to True
                if dp[i - len(w)] and s[i - len(w): i] == w:
                    dp[i] = True


        #return the last item since that will check all possible combinations if there is a combo of True the last word will be True
        return dp[-1]
