

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        l_minus_r = 0
        count = 0
        for ch in s:
            l_minus_r += 1 if ch == "L" else -1
            count += 1 if l_minus_r == 0 else 0
        return count


