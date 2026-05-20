

class Solution:
    def makeFancyString(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        out = []
        for ch in s:
            if not (len(out) > 2 and ch == out[-1] and ch == out[-2]):
                out.append(ch)
        return "".join(out)


