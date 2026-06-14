

class Solution:
    def minimumChairs(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        c = b = 0
        for ch in s:
            c += 1 if ch == "E" else -1
            b = max(b, c)
        return b


