

class Solution:
    def maxPower(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        best = 1
        cur = 1
        prev = None
        for ch in s:
            if prev is not None and prev == ch:
                cur += 1
            else:
                cur = 1
            best = max(best, cur)
            prev = ch
        return best


