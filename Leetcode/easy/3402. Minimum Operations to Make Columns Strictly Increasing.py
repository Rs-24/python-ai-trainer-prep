

class Solution:
    def minimumOperations(self, grid: list[list]) -> int:
        # Time: O(n^2)
        # Space: O(1)
        t = 0
        for c in range(len(grid[0])):
            p = grid[0][c]
            for r in range(1, len(grid)):
                if grid[r][c] <= p:
                    t += p - grid[r][c] + 1
                    p = p + 1
                else:
                    p = grid[r][c]
        return t


