

class Solution:
    def countKeyChanges(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        return sum(1 for i in range(1, len(s)) if s[i - 1].lower() != s[i].lower())


