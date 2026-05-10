

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # Time: O(1)
        # Space: O(1)
        if a == b:
            return -1
        return max(len(a), len(b))


