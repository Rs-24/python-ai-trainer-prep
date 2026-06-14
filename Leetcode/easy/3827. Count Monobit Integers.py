

class Solution:
    def countMonobit(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        c = x = 0
        while x <= n:
            c += 1
            x = (x << 1) | 1
        return c


