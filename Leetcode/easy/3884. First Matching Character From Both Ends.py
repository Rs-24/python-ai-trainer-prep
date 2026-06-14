

class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        for i in range((len(s) + 1) // 2):
            if s[i] == s[len(s) - i - 1]:
                return i
        return -1


