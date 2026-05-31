

class Solution:
    def maximumValue(self, strs: list) -> int:
        # Time: O(n)
        # Space: O(n)
        b = 0
        for s in strs:
            c = int(s) if all(ch.isdigit() for ch in s) else len(s)
            b = max(b, c)
        return b


