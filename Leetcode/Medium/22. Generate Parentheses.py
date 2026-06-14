

class Solution:
    def generateParenthesis(self, n: int) -> list:
        # Time: O(n^2)
        # Space: O(n)
        out = []
        s = [([""], 0, 0)]
        while s:
            e, o, c = s.pop()
            if len(e) == 2 * n:
                out.append("".join(e))
                continue
            if o < n:
                s.append((e + ["("], o + 1, c))
            if c < o:
                s.append((e + [")"], o, c + 1))
        return out


