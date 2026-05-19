

class Solution:
    def maxDepth(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        cur = best = 0
        for ch in s:
            cur += 1 if ch == "(" else -1 if ch == ")" else 0
            best = max(best, cur)
        return best


