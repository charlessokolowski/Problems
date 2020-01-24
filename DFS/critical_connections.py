"""
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.



Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
"""



from collections import defaultdict

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """

        self.timer = 0
        timer_list = [n] * n
        parent_list = [n] * n
        visited = [False] * n

        #defaultdict stores the mapping to values as a list so you dont need to establish blank lists for each key
        graphMap = defaultdict(list)
        result = []

        #iterate over each elements and unpack each element from connections and map each node to its neighbors
        for x, y in connections:
            graphMap[x].append(y)
            graphMap[y].append(x)

        def dfs(node, result):

            #as soon as we start dfs the visited lists current node is set to true
            visited[node] = True
            #set the current nodes timer to the currnet timer in the loop
            curr_node_timer = self.timer
            #set the timer_list current position to this timer
            timer_list[node]  = self.timer

            #once we have our current vals timer increment it by one
            self.timer += 1


            #iterate over the neighbors of our current node
            for neighbor in graphMap[node]:
                #if its not been visited as in if the current visited position is still False the set our current parent_list postion to the node then call dfs on the current neighbor`
                if not visited[neighbor]:
                    parent_list[neighbor] = node
                    dfs(neighbor, result)

                    #after the above dfs exits we check the timer value of our neighbor, if it is greater than our current node add the node and the neighbor to a list
                    if timer_list[neighbor] > curr_node_timer:
                        result.append([node, neighbor])
                #if original nodes parent is not the neighbor set the timer_list at the current postion to the minimum of two of them
                if parent_list[node] != neighbor:
                    timer_list[node] = min(timer_list[node], timer_list[neighbor])

        dfs(0, result)
        return result
