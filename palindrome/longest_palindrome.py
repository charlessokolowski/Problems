"""
Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.

Test case = "abccccdd"
"""




class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        # must take care of corner case when the list is empty
        if not s:
            return 0

        wordMap = {}

        for i in s:
            # this takes care of the doubles in the string. Ex. if theyre 2 a's it would remove both of them.
            if i in wordMap:
                del wordMap[i]
            else:
            #if the letter is not in the dictionary then it adds it to the dictionary as a fresh key.
                wordMap[i] = True
        if len(wordMap) == 0:
            #if we have removed all the objects from the dictionary then it all is doubles so the whole thing can be a palindrome thus return length of the original
            return len(s)
        else:
            # compares the elements of the dictonary if they are in the dictonary, they are only single letters, add one to this because it is an odd palindrome.
            return len(s) - len(wordMap) + 1
