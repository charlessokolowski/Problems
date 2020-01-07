"""
There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peak if:

A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.

Example
Example 1:
	Input:  [1, 2, 1, 3, 4, 5, 7, 6]
	Output:  1 or 6

	Explanation:
	return the index of peek.


Example 2:
	Input: [1,2,3,4,1]
	Output:  3
"""


class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):

        left, right = 0, len(A) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            #need to check each of the paths left and right for each step to see if it is increasing. otherwise just return right since it will be equal to mid so it can keep going
            if A[mid] < A[mid + 1]:
                if A[mid - 1] < A[mid]:
                    left = mid
                else:
                    right = mid
            elif A[mid] > A[mid + 1]:
                if A[mid - 1] > A[mid]:
                    right = mid
                else:
                    left = mid
            else:
                right = mid
        #compare values and return the largest of the 2
        if A[left] > A[right]:
            return left
        else:
            return right
