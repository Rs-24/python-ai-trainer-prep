

class Solution:
    def makeGood(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        out = []
        for ch in s:
            if out and abs(ord(out[-1]) - ord(ch)) == 32:
                out.pop()
            else:
                out.append(ch)
        return "".join(out)


