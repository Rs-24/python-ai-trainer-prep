

class Solution:
    def scoreOfString(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        return sum(abs(ord(s[i]) - ord(s[i - 1])) for i in range(1, len(s)))


