

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Time: O(n)
        # Space: O(n)
        t = (len(b) + len(a) - 1) // len(a)
        s = a * t
        if b in s:
            return t
        s += a
        if b in s:
            return t + 1
        return -1


