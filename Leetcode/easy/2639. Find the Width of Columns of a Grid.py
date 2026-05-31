

class Solution:
    def findColumnWidth(self, grid: list[list]) -> list:
        # Time: O(n^2)
        # Space: O(n)
        o = []
        for c in range(len(grid[0])):
            b = 0
            for r in range(len(grid)):
                b = max(b, len(str(grid[r][c])))
            o.append(b)
        return o


