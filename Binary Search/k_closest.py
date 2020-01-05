"""
Given target, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.

Example
Example 1:

Input: A = [1, 2, 3], target = 2, k = 3
Output: [2, 1, 3]
Example 2:

Input: A = [1, 4, 6, 8], target = 3, k = 3
Output: [4, 1, 6]
"""



class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):

        result = []

        #helper function that returns the index of the right most of the time except when the target is lower or equal to the left more elenment
        def binSearch(A, target):
            left, right = 0, len(A) - 1

            while left + 1 < right:
                mid = (left + right) // 2
                if A[mid] < target:
                    left = mid
                else:
                    right = mid

            if target <= A[left]:
                return left

            return right

        #helper to use booleans as a switch to test of the left or right is valid
        def expand(A, left, right):
            if left < 0:
                return False
            if right > len(A) - 1:
                return True
            return target - A[left] <= A[right] - target

        right = binSearch(A, target)
        left = right - 1

        #iterate through the expand k times, and append each time to the result list and increment the left or right
        for _ in range(k):
            if expand(A, left, right):
                result.append(A[left])
                left -= 1
            else:
                result.append(A[right])
                right += 1
        return result
