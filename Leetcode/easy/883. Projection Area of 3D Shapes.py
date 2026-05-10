

class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        # Time: O(m * n), m = len(grid), n = len(grid[0])
        # Space: O(1)
        xy = sum(1 for row in grid for val in row if val > 0)
        xz = sum(max(row) for row in grid)
        yz = 0
        for c in range(len(grid[0])):
            best = 0
            for r in range(len(grid)):
                best = max(best, grid[r][c])
            yz += best
        return xy + xz + yz


