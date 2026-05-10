

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(n)
        return s in (s + s)[1:-1]


