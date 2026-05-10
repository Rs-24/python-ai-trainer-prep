

class Solution:
    def binaryGap(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        best = 0
        cur = None
        while n > 0:
            if n & 1 == 1:
                if cur is not None:
                    best = max(best, cur)
                cur = 1
            else:
                if cur is not None:
                    cur += 1
            n >>= 1
        return best


