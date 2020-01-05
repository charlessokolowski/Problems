"""
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.

"""




from collections import deque


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        nodeMap={}

        #bub function that returns a list which is nodes
        def bfs(node):
            #add root node to visited and queue
            visited = set([node])
            queue = deque([node])
            while queue:
                eachNode = queue.popleft()
                #iterates through each neighbor
                for i in eachNode.neighbors:
                    if i not in visited:
                        visited.add(i)
                        queue.append(i)
            return visited

        #list returned from the bfs sub function
        nodeList = bfs(node)

        #iterate through new list and makes keys with each element of that list mapped to new nodes of the game value
        for i in nodeList:
            nodeMap[i]= Node(i.val,[])


        #iterate through each neighbor and add them as new nodes to the nodes as new nieghbors 
        for i in nodeList:
            for j in i.neighbors:
                nodeMap[i].neighbors.append(nodeMap[j])
        return nodeMap[node]
