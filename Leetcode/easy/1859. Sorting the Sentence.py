

class Solution:
    def sortSentence(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        s = s.split()
        out = [""] * len(s)
        for w in s:
            out[int(w[-1]) - 1] = w[:-1]
        return " ".join(out)


