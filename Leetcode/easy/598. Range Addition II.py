

class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        # Time: O(N), N = len(ops)
        # Space: O(1)
        for x, y in ops:
            m = min(m, x)
            n = min(n, y)
        return m * n


