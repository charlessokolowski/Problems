"""
Ugly number is a number that only have prime factors 2, 3 and 5.

Design an algorithm to find the nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

Example
Example 1:

Input: 9
Output: 10
Example 2:

Input: 1
Output: 1

"""



import heapq

class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):

        heap = [1]

        visited = set([1])

        val = None

        #pop first val from the heap
        for i in range(n):
            val = heapq.heappop(heap)
            #iterate over our 2,3,5 and for the current val multiply them
            for factor in [2, 3, 5]:
                #if they are not in the vistied set push it and add it to the set
                if val * factor not in visited:
                    heapq.heappush(heap, factor * val)
                    visited.add(factor * val)
        #if we are done with the for loop we can just return our val
        return val
