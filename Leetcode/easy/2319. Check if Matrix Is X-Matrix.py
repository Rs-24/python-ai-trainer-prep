

class Solution:
    def checkXMatrix(self, grid: list[list]) -> bool:
        # Time: O(n^2)
        # Space: O(1)
        n = len(grid)
        for r in range(n):
            for c in range(n):
                if (r == c or r == n - 1 - c) == (grid[r][c] == 0):
                    return False
        return True


