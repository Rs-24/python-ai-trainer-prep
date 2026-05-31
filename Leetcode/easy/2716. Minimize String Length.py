

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)
        return len(set(s))


