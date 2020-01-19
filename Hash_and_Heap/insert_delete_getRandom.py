"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();

"""

import random


class RandomizedSet:

    def __init__(self):
        self.newSet = []
        self.newMap = {}
        self.count = 0


    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """

    #if the value is not in our map we can add it to the map and the list if we do that increment the count by one and add it to both the list and the map, add it to the map and map it to the count
    def insert(self, val):
        if val not in self.newMap:
            self.newSet.append(val)
            self.newMap[val] = self.count
            self.count += 1
            return True
        else:
            return False

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    #if it not in the map we cannot delete it so return false otehrwise store the value of our last index swap the target val with our last index and pop the new last index and then replace the base element with the value from our old element in the map which was the old elements index
    def remove(self, val):
        if val not in self.newMap:
            return False
        else:
            base = self.newSet[-1]
            self.newSet[self.newMap[val]], self.newSet[-1] = self.newSet[-1], self.newSet[self.newMap[val]]
            self.newSet.pop()

            self.newMap[base] = self.newMap[val]

            #then delete our old value from the map and lower the count by 1
            del self.newMap[val]

            self.count -= 1
            return True
    """
    @return: Get a random element from the set
    """
    def getRandom(self):

        #generate random number from 0 to our count -1 since our count is the length of out list
        sub = random.randint(0, self.count - 1)

        #just call our random number on our list
        return self.newSet[sub]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
