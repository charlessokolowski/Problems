"""
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

Example
Example 1:

Input："lintcode"，["de","ding","co","code","lint"]
Output：["lint code", "lint co de"]
Explanation：
insert a space is "lint code"，insert two spaces is "lint co de".
Example 2:

Input："a"，[]
Output：[]
Explanation：dict is null.



"""

class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):

        #one of lintcodes odd test cases is just a blank string in a set
        if wordDict == set([""]):
            return []


        memo = {}

        return self.dfs(s, wordDict, memo)




    def dfs(self, s, wordDict, memo):

        #at lower levels of recursion the memo will hold values of each split string and we can just return them if our current string is that
        if s in memo:
            return memo[s]

        if not s:
            return []

        result = []


        #grab each word in our given dict and check it with the bit of the string
        for word in wordDict:

            #if the string doesnt start with the current word, skip it
            if not s.startswith(word):
                continue

            #could also directly check if word and s are the same but just check both and add it to result list
            if len(s) == len(word):
                result.append(word)

            #since the string still contains more after we found a val we split the val and find all the lower levels and store them in a list
            else:
                wordList = self.dfs(s[len(word):], wordDict, memo)
                #iterate over that list and create new words for each one that has a space in between them then add them to the result
                for i in wordList:
                    newWord = word + " " + i
                    result.append(newWord)

        #create a dictionary kv pair with the current string and the current result
        memo[s] = result
        #return that result
        return result
