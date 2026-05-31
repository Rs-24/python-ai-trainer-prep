

class Solution:
    def maxDivScore(self, nums: list, divisors: list) -> int:
        # Time: O(n^2)
        # Space: O(1)
        b, v = 0, None
        for n in nums:
            c = 0
            for d in divisors:
                c += d % n == 0
            if c > b:
                b = c
                v = n
            elif c == b and v is not None and n < v:
                v = n
        return v


