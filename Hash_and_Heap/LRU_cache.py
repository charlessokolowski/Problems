"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
Finally, you need to return the data from each get.

Example
Example1

Input:
LRUCache(2)
set(2, 1)
set(1, 1)
get(2)
set(4, 1)
get(1)
get(2)
Output: [1,-1,1]
Explanation：
cache cap is 2，set(2,1)，set(1, 1)，get(2) and return 1，set(4,1) and delete (1,1)，because （1,1）is the least use，get(1) and return -1，get(2) and return 1.
Example 2:

Input：
LRUCache(1)
set(2, 1)
get(2)
set(3, 2)
get(2)
get(3)
Output：[1,-1,2]
Explanation：
cache cap is 1，set(2,1)，get(2) and return 1，set(3,2) and delete (2,1)，get(2) and return -1，get(3) and return 2.

"""

#create a class called listNode1 has previous and next placeholders
class ListNode1:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):

        #initalize capacity inside of here so we an use it in other parts of the function
        self.capacity = capacity

        self.dictMap = {}

        #create blank head and tail nodes
        self.head = ListNode1(0, 0)
        self.tail = ListNode1(0, 0)

        #link the head and the tail, heads next points to tail and tails previous points ot head`
        self.head.next = self.tail
        self.tail.prev = self.head


    """
    @param: key: An integer
    @return: An integer
    """

    #get checks if it is in the dictMap if it is not return -1 if it is remove that node and add it back in and reutnr the value from that node
    def get(self, key):
        if key not in self.dictMap:
            return - 1

        node = self.dictMap[key]
        self.removeNode(node)
        self.addNode(node)
        return node.val

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    #if the key is in the dictmap we remove it from the dictMap
    def set(self, key, value):

        if key in self.dictMap:
            self.removeNode(self.dictMap[key])

        #then we create a node with those key and val pairs and add it using our addnode function and add it to the map
        node = ListNode1(key, value)
        self.addNode(node)
        self.dictMap[key] = node

        #after the length of the dictMap is greater than we grab the value of the node to be removed, since we push the nodes in as a tails previous our last viisted node will always be our heads next so we remove that node
        if len(self.dictMap) > self.capacity:
            headNext = self.head.next
            self.removeNode(headNext)
            del self.dictMap[headNext.key]

    #add node stores the previous tails node points its next at our current node, points to the tail from our current node, sets our current nodes previous pointer to the first (previous) node and sets the tails previous to our current node
    def addNode(self, node):
        previous = self.tail.prev
        previous.next = node
        node.next = self.tail
        node.prev = previous
        self.tail.prev = node


    #first stores our previous and next nodes, then points the previous next as the nextnode and the nextnode prev as the previous
    def removeNode(self, node):
        previous = node.prev
        nextNode = node.next

        previous.next = nextNode
        nextNode.prev = previous
