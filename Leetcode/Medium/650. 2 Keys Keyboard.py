

class Solution:
    def minSteps(self, n: int) -> int:
        # Time: O(sqrt(n))
        # Space: O(1)
        a, t = 0, 2
        while t * t <= n:
            while n % t == 0:
                a += t
                n //= t
            t += 1
        a += n * (n > 1)
        return a


