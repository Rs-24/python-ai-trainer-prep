

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # Time: O(n^2)
        # Space: O(n)
        s = list(s)
        while len(s) > 2:
            t = []
            for i in range(len(s) - 1):
                t.append((int(s[i]) + int(s[i + 1])) % 10)
            s[:] = t
        return s[0] == s[1]


