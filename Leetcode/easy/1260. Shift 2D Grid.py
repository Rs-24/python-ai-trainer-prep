

class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        # Time: O(m * n), m = len(grid), n = len(grid[0])
        # Space: O(m * n)
        m, n = len(grid), len(grid[0])
        out = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                idx = (r * n + c + k) % (m * n)
                out[idx // n][idx % n] = grid[r][c]
        return out


