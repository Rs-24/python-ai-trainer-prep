

class Solution:
    def deleteGreatestValue(self, grid: list[list]) -> int:
        # Time: O(n^2 log n)
        # Space: O(1)
        for r in grid:
            r.sort()
        s = 0
        for c in range(len(grid[0]) - 1, -1, -1):
            s += max(grid[r][c] for r in range(len(grid)))
        return s


