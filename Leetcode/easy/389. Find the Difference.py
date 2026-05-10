

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Time: O(m + n), m = len(s), n = len(t)
        # Space: O(1)
        out = 0
        for ch in s:
            out ^= ord(ch)
        for ch in t:
            out ^= ord(ch)
        return chr(out)


