

class Solution:
    def maxAreaOfIsland(self, grid: list[list]) -> int:
        # Time: O(m * n)
        # Space: O(m * n)
        m, n = len(grid), len(grid[0])
        a = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    s = [(r, c)]
                    grid[r][c] = 0
                    t = 0
                    while s:
                        i, j = s.pop()
                        t += 1
                        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            if 0 <= i + di < m and 0 <= j + dj < n and grid[i + di][j + dj] == 1:
                                grid[i + di][j + dj] = 0
                                s.append((i + di, j + dj))
                    a = max(a, t)
        return a


