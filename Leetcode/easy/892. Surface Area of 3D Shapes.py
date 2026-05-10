

class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        # Time: O(m * n), m = len(grid), n = len(grid[0])
        # Space: O(1)
        base = sum(1 for row in grid for val in row if val > 0)
        side1 = sum(max(row) for row in grid)
        side2 = 0
        for c in range(len(grid[0])):
            best = 0
            for r in range(len(grid)):
                best = max(best, grid[r][c])
            side2 += best
        return 2 * (base + side1 + side2)


