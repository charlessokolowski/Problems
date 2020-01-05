"""
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.

"""



from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        courseMap = {}
        courseNeighbors = {}
        Lis = []

        if not prerequisites:
            return True

        #create dictionaries with blank values
        for i in range(numCourses):
            courseMap[i] = 0
            courseNeighbors[i] = []

        #fill the values of each key using prerequisites
        for course, prereq in prerequisites:
            courseNeighbors[prereq].append(course)
            courseMap[course] += 1


        #if Dictonary value is 0 add to queue and list
        queue = deque([])
        for i in courseMap:
            if courseMap[i] == 0:
                queue.append(i)
                Lis.append(i)

        while queue:
            value = queue.popleft()
            #iterate over each value in list of nieghbors and subtract one from each
            for i in courseNeighbors[value]:
                courseMap[i] -= 1
                #if the value is 0 add to queue
                if courseMap[i] == 0:
                    queue.append(i)
                    Lis.append(i)
        #the list will have all the elements for each 0 degree so it has to match
        return len(Lis) == numCourses
