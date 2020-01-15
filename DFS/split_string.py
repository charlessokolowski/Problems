"""
Give a string, you can choose to split the string after one character or two adjacent characters, and make the string to be composed of only one character or two characters. Output all possible results.

Example
Example1

Input: "123"
Output: [["1","2","3"],["12","3"],["1","23"]]

first round path =["1"]

second s = "23" and path is ["1", "2"]

third rounds = "3" path = ["3"] and path is ["1", "2", "3"]

fourth round s = "" so we append ["1", "2", "3"] to result

5th round go back to third round and pop the "3" from path then increment i t0 1 and exit that loop

6th round goes back to second round and pop "2" from path then increment 1 to 1 and since the string is "23" it wont exit so we call the dps with "1" and append that to path so it becomes [1, 23]



Example2

Input: "12345"
Output: [["1","23","45"],["12","3","45"],["12","34","5"],["1","2","3","45"],["1","2","34","5"],["1","23","4","5"],["12","3","4","5"],["1","2","3","4","5"]]
"""



class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):

        result = []
        path = []
        self.dfs(s, result, path)
        return result


    #base case for recursion is when the lower level is the string ""
    def dfs(self, s, result, path):
        if s == "" :
            #use [:] to call all elements in list
            result.append(path[:])
        #use range 2 since we are checking 2 strings
        for i in range(2):

            #if the string can be split furher continue
            if i + 1 <= len(s):
                #appends the current strings from the current index + 1 to the end of the path
                path.append(s[i + 1 :])
                #recursively calls the remainder of the string from above
                self.dfs(s, result, s[: i + 1])
                #after the above round of recursion is completed then pop the current rightmost item from the list
                path.pop()
