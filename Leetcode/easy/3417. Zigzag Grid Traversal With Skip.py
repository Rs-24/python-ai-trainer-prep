

class Solution:
    def zigzagTraversal(self, grid: list[list]) -> list:
        # Time: O(n^2)
        # Space: O(n^2)
        out = []
        r = False
        t = True
        for row in grid:
            if r:
                row.reverse()
            for x in row:
                if t:
                    out.append(x)
                t = not t
            r = not r
        return out


