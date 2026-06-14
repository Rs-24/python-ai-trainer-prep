

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        c = [0] * 10
        t = n
        while t > 0:
            c[t % 10] += 1
            t //= 10
        m = min(c)
        for x, f in enumerate(c):
            if f == m:
                return x


