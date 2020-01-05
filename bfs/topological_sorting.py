"""
Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

Example
For graph as follow:


The topological order can be:

[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...

"""




from collections import deque



"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        inDegree = {}
        neighborsMap = {}
        result = []

        #iterate through graph and create 2 dictonaries one with the keys as each node with no val and the other with the node mapped to beighbors
        for i in graph:
            inDegree[i] = 0
            neighborsMap[i] = i.neighbors

        #gets the edges for each neighbor using the neighborsMap
        for i in neighborsMap:
            for j in i.neighbors:
                inDegree[j] += 1

        #adds all values that are 0
        queue= deque([])
        for i in inDegree:
            if inDegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            result.append(node)
            #if there are no more edges it can be added to the qeueu to check the next nodes edges
            for i in node.neighbors:
                inDegree[i] -= 1
                if inDegree[i] == 0:
                    queue.append(i)
        return result
