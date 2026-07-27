

class Solution:
    def matrixScore(self, grid: list) -> int:
        # Time: O(m * n)
        # Space: O(1)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1
        for j in range(n):
            t = sum(grid[i][j] for i in range(m))
            if t < m - t:
                for i in range(m):
                    grid[i][j] ^= 1
        a = 0
        for i in range(m):
            for j in range(n):
                a += grid[i][j] * (2 ** (n - j - 1))
        return a


        