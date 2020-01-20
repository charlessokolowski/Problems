"""
Given an integer array, find the top k largest numbers in it.

Example
Example1

Input: [3, 10, 1000, -99, 4, 100] and k = 3
Output: [1000, 100, 10]
Example2

Input: [8, 7, 6, 5, 4, 3, 2, 1] and k = 5
Output: [8, 7, 6, 5, 4]

"""
import heapq


class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):

        #create 2 lists the heap will hold our unsorted values and the reuslt list will hold the sorted
        heap = []
        result = []

        for i in range(len(nums)):

            #iterate over the items in teh list and push them as a heap the heap list as negative so the largest will be stored at the top
            heapq.heappush(heap, -nums[i])

        #only need k elements so pop the largest neagitve from the heap which will be the biggest neagitve, then add it to our result list
        for i in range(k):
            result.append(-heapq.heappop(heap))

        return result
