

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # Time: O(n)
        # Space: O(n)
        b = 0
        d = {0: 0}
        for p in input.split("\n"):
            depth = p.count("\t")
            t = p[depth:]
            if "." in t:
                b = max(b, d[depth] + len(t))
            else:
                d[depth + 1] = d[depth] + len(t) + 1
        return b


