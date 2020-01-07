"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Example
Example 1:

Input: [4, 5, 1, 2, 3] and target=1,
Output: 2.
Example 2:

Input: [4, 5, 1, 2, 3] and target=0,
Output: -1.
"""

class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):

        if not A:
            return -1

        left, right = 0, len(A) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            #checks if the mid is less than the right if it is then it is increasing in that range
            if A[mid] < A[right]:
                #if the target is in the range of the mid and right then set the left to the mid otherwise set right to mid
                if A[mid] <= target <= A[right]:
                    left = mid
                else:
                    right = mid
            else:
                #does the opposite for the left as above
                if A[left] <= target <= A[mid]:
                    right = mid
                else:
                    left = mid
        #checks if either are the target otherwise return -1
        if A[left] == target:
            return left
        if A[right] == target:
            return right
        else:
            return -1
