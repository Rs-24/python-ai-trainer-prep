

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Time: O(n)
        # Space: O(n)
        if numRows == 1 or numRows >= len(s):
            return s
        r = [[] for _ in range(numRows)]
        i = 0
        d = 1
        for ch in s:
            r[i].append(ch)
            if i == numRows - 1:
                d = -1
            elif i == 0:
                d = 1
            i += d
        return "".join("".join(t) for t in r)


