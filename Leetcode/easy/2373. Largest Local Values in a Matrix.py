

class Solution:
    def largestLocal(self, grid: list[list]) -> list[list]:
        # Time: O(n^2)
        # Space: O(n^2)
        def max_val(r: int, c: int) -> int:
            best = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    best = max(best, grid[r + i][c + j])
            return best
        n = len(grid)
        out = [[0] * (n - 2) for _ in range(n - 2)]
        for r in range(1, n - 1):
            for c in range(1, n - 1):
                out[r - 1][c - 1] = max_val(r, c)
        return out


