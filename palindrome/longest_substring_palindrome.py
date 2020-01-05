"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Test case s = "babad"
output = "bab" or "aba"

"""



class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        if len(s) == 1:
            return s

        #sub function that uses while loop to return the index position of the current substrings longest palindrome
        def getIndex(left, right):
            #left and right cannot be out of range abd they both need to be the same in order to continue while loop
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            #since while loop ended return the previous run
            return left + 1, right - 1


        maxLen = 0
        substring = ""

        for i in range(len(s) - 1):
            #check if 2 letters are the same and pass to our helper
            if s[i] == s[i + 1]:
                #unpacks both values from helper
                left, right = getIndex(i, i + 1)
                #need to add one to the values since left and right are index values
                if right - left + 1 > maxLen:
                    maxLen = right - left + 1
                    substring = s[left : right + 1]
            left, right = getIndex(i, i)
            if right - left + 1 > maxLen:
                maxLen = right - left + 1
                substring = s[left : right + 1]
        return substring
