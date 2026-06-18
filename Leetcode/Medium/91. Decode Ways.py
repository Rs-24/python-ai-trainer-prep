

class Solution:
    def numDecodings(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        if not s or s[0] == "0":
            return 0
        n = len(s)
        a, b = 1, 1
        for i in range(1, n):
            t = 0
            if s[i] != "0":
                t += b
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                t += a
            a, b = b, t
        return b


