"""
Calculate the an % b where a, b and n are all 32bit non-negative integers.

Example
For 231 % 3 = 2

For 1001000 % 1000 = 0
"""

class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        #remember to mod everything even the one for the return of 0
        if n == 0:
            return 1 % b

        def compute(a, b, n):
            if n == 1:
                return a % b
            #recursive call of compute decreasing n each time
            half = compute(a, b, n // 2)
            if n % 2 == 0:
                #all mods of % b 
                return (half * half) % b
            else:
                return (half * half * a) % b
        if n < 0:
            return compute(1/a, b, -n)
        else:
            return compute(a, b, n)
