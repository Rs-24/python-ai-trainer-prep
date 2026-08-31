

class Solution:
    def largest1BorderedSquare(self, grid: list) -> int:
        # Time: O(m * n * min(m, n))
        # Space: O(m * n)
        m, n = len(grid), len(grid[0])
        r = [[0] * (n + 1) for _ in range(m + 1)]
        d = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    r[i][j] = 1 + r[i][j + 1]
                    d[i][j] = 1 + d[i + 1][j]
        for l in range(min(m, n), 0, -1):
            for i in range(m - l + 1):
                for j in range(n - l + 1):
                    if r[i][j] < l or r[i + l - 1][j] < l or d[i][j] < l or d[i][j + l - 1] < l:
                        continue
                    return l * l
        return 0


