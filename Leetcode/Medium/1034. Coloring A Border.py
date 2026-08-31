

class Solution:
    def colorBorder(self, grid: list, row: int, col: int, color: int) -> list:
        # Time: O(m * n)
        # Space: O(m * n)
        m, n = len(grid), len(grid[0])
        x = grid[row][col]
        s = set()
        a = []
        def dfs(r: int, c: int) -> None:
            s.add((r, c))
            t = False
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (not (0 <= r + dr < m and 0 <= c + dc < n)) or grid[r + dr][c + dc] != x:
                    t = True
                elif (r + dr, c + dc) not in s:
                    dfs(r + dr, c + dc)
            if t:
                a.append((r, c))
        dfs(row, col)
        for r, c in a:
            grid[r][c] = color
        return grid


