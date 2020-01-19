"""
Find the first unique character in a given string. You can assume that there is at least one unique character in the string.

Example
Example 1:
	Input: "abaccdeff"
	Output:  'b'

	Explanation:
	There is only one 'b' and it is the first one.


Example 2:
	Input: "aabccd"
	Output:  'b'

	Explanation:
	'b' is the first one.
"""
class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):

        letterMap = {}
        #create map that has count of the words in it
        for i in range(len(str)):
            if str[i] in letterMap:
                letterMap[str[i]] += 1
            else:
                letterMap[str[i]] = 1

        #iterate over the string and use that element as a key in our dictionary if it equals 1 it is the first item with count one so return it
        for i in str:
            if letterMap[i] == 1:
                return i
