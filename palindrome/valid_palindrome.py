"""
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

Test case = Input: "A man, a plan, a canal: Panama"
Output: true

"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # use two pointers for start and end
        beg,end = 0, len(s) - 1
        while beg < end :
            #checks to see if the char is a letter or number and use while loop to iterate until it is one or the other.
            while not s[beg].isalnum() and beg < end:
                beg += 1
            while not s[end].isalnum() and beg < end:
                end -= 1
            #checks each char against its counter part if one is not the same can return false immediately
            if s[beg].lower() != s[end].lower():
                return False
            #if the chars at the current beg and end match increment both of them closer to the center of the world
            else:
                beg += 1
                end -= 1
        #if the while loop exits it is a valid palindrome so return true
        return True
