"""
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, output sequence in dictionary order.
Transformation rule such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
Example
Example 1:

Input：start = "a"，end = "c"，dict =["a","b","c"]
Output：[["a","c"]]
Explanation：
"a"->"c"
Example 2:

Input：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
Output：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation：
1."hit"->"hot"->"dot"->"dog"->"cog"
2."hit"->"hot"->"lot"->"log"->"cog"
The dictionary order of the first sequence is less than that of the second.
"""


from collections import deque

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):


        #add both start and end to dict since it is a set it doesnt matter if they are in already
        dict.add(start)
        dict.add(end)

        distance = {}

        #call bfs on end word with a distance map that we will store the disance from the word to the next one as another 1
        self.bfs(end, distance, dict)

        #initialize the path with the start word
        result, path = [], [start]

        #dfs needs to get everything
        self.dfs(start, end, dict, distance, result, path)

        return result


    def bfs(self, start, distance, dict):

        #start the distance map with the current word mapped to 0 as the value
        distance[start] = 0

        #then add that word to the que
        queue = deque([start])

        while queue:

            word = queue.popleft()

            #pass our popped word down to our modWord function and it will return a sublist with all the possible combinations of current word that is one letter different
            wordsList = self.modWord(word, dict)

            #iterate through the list if it is not in the distance map already add it to the distance map and and the queue, the value is the previous levels value plus 1
            for i in wordsList:
                if i not in distance:
                    queue.append(i)
                    distance[i] = distance[word] + 1


    def modWord(self, word, dict):

        wordsList=[]

        #iterate through each letter of the current word and each letter of the alphabet
        for eachLetter in range(len(word)):
            for letter in "abcdefghijklmnopqrstuvwxyz":
                #makes a new copy of a word for each iteration of the word changing one letter at a time.
                newWord = word[ : eachLetter] + letter + word[eachLetter +1: ]
                #if the newword isnt the current word and its in our original set then we can add it to the list we will pass to our other functions
                if newWord != word and newWord in dict:
                    wordsList.append(newWord)

        return wordsList


    def dfs(self, start, end, dict, distance, result, path):

        #base case is when the current word that starts the dfs is equal to the end word
        if start == end:
            result.append(path[:])
            return

        #take all possible permutations of the start word
        wordsList = self.modWord(start, dict)

        #iterate through that list and check if the distance is greater than 1 if it is ignore it, otherwise if it is, add to the path and pass the new word to the dfs again then once the dfs is done pop last element of path
        for newWord in wordsList:
            if distance[newWord] + 1 != distance[start]:
                continue

            path.append(newWord)
            self.dfs(newWord, end, dict, distance, result, path)
            path.pop()
