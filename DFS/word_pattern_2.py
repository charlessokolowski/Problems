"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.(i.e if a corresponds to s, then b cannot correspond to s. For example, given pattern = "ab", str = "ss", return false.)

Example
Example 1

Input:
pattern = "abab"
str = "redblueredblue"
Output: true
Explanation: "a"->"red","b"->"blue"
Example 2

Input:
pattern = "aaaa"
str = "asdasdasdasd"
Output: true
Explanation: "a"->"asd"
Example 3

Input:
pattern = "aabb"
str = "xyzabcxzyabc"
Output: false
"""
class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):

        mapping = {}

        visited = set()

        return self.dfs(pattern, str, mapping, visited)

    def dfs(self, pattern, str, mapping, visited):

        #smart way of saying if not pattern string is also false
        if not pattern:
            return not str

        #pulls the first element from the pattern string
        char = pattern[0]

        #checks if it is the map if it is, then proceed
        if char in mapping:
            #gets the current str from the current char if it it doesnt start with the str w then return false else return the list split from the length of the current char to the the end of the current string input
            w = mapping[char]
            if not str.startswith(w):
                return False
            return self.dfs(pattern[1:], str[len(w):], mapping, visited)

        #iterate over the string if it is not in the map
        for i in range(len(str)):
            #w will go from the index +1 so when it repeats for failed letters it will increment the word until it finds a repeat letter
            w = str[: i + 1]
            #if the w is in visited just ski[]
            if w in visited:
                continue
            #otherwise add it to our visted set and set the current maps char to the w
            visited.add(w)
            mapping[char] = w

            #if the string passes true repeat until until you get a char that is in the map
            if self.dfs(pattern[1:], str[i+1 :], mapping, visited):
                return True

            #if the above recursion fails delete the current char and remove it from the visited set
            del mapping[char]
            visited.remove(w)

        #if the above for loop exits without there ever being a completed set return false
        return False
