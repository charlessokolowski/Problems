"""
Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, output the length of the sequence.
Transformation rule such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary. (Start and end words do not need to appear in the dictionary )
Example
Example 1:

Input：start = "a"，end = "c"，dict =["a","b","c"]
Output：2
Explanation：
"a"->"c"
Example 2:

Input：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
Output：5
Explanation：
"hit"->"hot"->"dot"->"dog"->"cog"

"""


from collections import deque

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):

        #important to add visitied set or will get inifite loop since it cab ve a cycle
        serialDict={}
        dict.add(end)
        visited = set()


        #creates keys with the seraialized versions of each word mapping to the actual word
        for i in dict:
            for j in range(len(i)):
                newSerial = i[:j] + "*" + i[j+1:]
                if newSerial in serialDict:
                    serialDict[newSerial].append(i)
                else:
                    serialDict[newSerial] = []
                    serialDict[newSerial].append(i)
        #add first item to queue and visited set, also important to add level to the queue at the same time to keep track of levels
        queue = deque([(start,1)])
        visited.add(start)
        while queue:
            (word, level) = queue.popleft()
            #serialize starting word and iterate though each version of this word
            for j in range(len(word)):
                newSerial = word[:j] + "*" + word[j+1:]
                if newSerial in serialDict:
                    #if the end word is in the list return the current level +1
                    if end in serialDict[newSerial]:
                        return level + 1
                    else:
                        #add the rest of the words from each sublist into the queue if they are not in the vusuted set
                        for i in serialDict[newSerial]:
                            if i not in visited:
                                queue.append((i, level + 1))
                                visited.add(word)
