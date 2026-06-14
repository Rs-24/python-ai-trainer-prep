

class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        for i in range(1, len(s)):
            if abs(int(s[i - 1]) - int(s[i])) > 2:
                return False
        return True


