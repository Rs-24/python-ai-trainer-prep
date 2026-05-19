

class Solution:
    def replaceDigits(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        def shift(c: str, x: int) -> str:
            return chr(ord(c) + x)       
        s = list(s)
        for i in range(0, len(s), 2):
            s[i + 1] = shift(s[i], int(s[i + 1]))
        return "".join(s)


