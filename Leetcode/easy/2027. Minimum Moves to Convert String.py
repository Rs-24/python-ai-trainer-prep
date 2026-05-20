

class Solution:
    def minimumMoves(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        count = 0
        i = 0
        while i < len(s):
            if s[i] == "X":
                count += 1
                i += 3
            else:
                i += 1
        return count


