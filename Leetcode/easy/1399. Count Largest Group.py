

class Solution:
    def countLargestGroup(self, n: int) -> int:
        # Time: O(n log n)
        # Space: O(n)
        def digit_sum(x: int) -> int:
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s
        d = {}
        for i in range(1, n + 1):
            s = digit_sum(i)
            d[s] = d.get(s, 0) + 1
        m = max(d.values())
        return sum(v == m for v in d.values())


