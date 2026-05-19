

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(1)
        i = 0
        while i < len(s) and s[i] == "1":
            i += 1
        while i < len(s) and s[i] == "0":
            i += 1
        while i < len(s):
            if s[i] == "1":
                return False
            i += 1
        return True


