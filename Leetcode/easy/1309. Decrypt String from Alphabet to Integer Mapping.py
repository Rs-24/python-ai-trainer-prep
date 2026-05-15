

class Solution:
    def freqAlphabets(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        out = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == "#":
                num = int(s[i - 2]) * 10 + int(s[i - 1])
                out.append(chr(ord("a") + num - 1))
                i -= 3
            else:
                num = int(s[i])
                out.append(chr(ord("a") + num - 1))
                i -= 1
        return "".join(reversed(out))


