

class Solution:
    def countPrimes(self, n: int) -> int:
        # Time: O(n log log n)
        # Space: O(n)
        if n <= 2:
            return 0
        p = [True] * n
        p[0] = p[1] = False
        x = 2
        while x * x < n:
            if p[x]:
                for m in range(x * x, n, x):
                    p[m] = False
            x += 1
        return sum(p)


