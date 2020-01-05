"""
Implement pow(x, n). (n is an integer.)

Example
Example 1:

Input: x = 9.88023, n = 3
Output: 964.498
Example 2:

Input: x = 2.1, n = 3
Output: 9.261
Example 3:

Input: x = 1, n = 0
Output: 1

"""

class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        if n == 0:
            return 1
        #sub function n ==1 is base case to end recursion
        def compute(x, n):
            if n == 1:
                return x
            #recursion variable lowers the n each time until n == 1
            recursion = compute(x, n // 2)
            #this is to check if it is odd or even, in the case of even it just multiplies the previous layer or recursion by itself if not multiply extra x
            if n % 2 == 0:
                return recursion * recursion
            else:
                return recursion * recursion * x

        #if n is negative need to turn it into fraction and negate the n per mmaths
        if n < 0:
            return compute(1/x, -n)
        else:
            return compute(x, n)
