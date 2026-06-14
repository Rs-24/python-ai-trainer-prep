

class Solution:
    def satisfiesConditions(self, grid: list[list]) -> bool:
        # Time: O(n^2)
        # Space: O(1)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r < len(grid) - 1 and grid[r][c] != grid[r + 1][c]:
                    return False
                if c < len(grid[0]) - 1 and grid[r][c] == grid[r][c + 1]:
                    return False
        return True


