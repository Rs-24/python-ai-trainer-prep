

class Solution:
    def pacificAtlantic(self, heights: list[list]) -> list[list]:
        # Time: O(m * n)
        # Space: O(m * n)
        if not heights:
            return []
        m, n = len(heights), len(heights[0])
        p, a = set(), set()
        def dfs(r, c, s):
            s.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= r + dr < m and 0 <= c + dc < n and (r + dr, c + dc) not in s and heights[r + dr][c + dc] >= heights[r][c]:
                    dfs(r + dr, c + dc, s)
        for c in range(n):
            dfs(0, c, p)
            dfs(m - 1, c, a)
        for r in range(m):
            dfs(r, 0, p)
            dfs(r, n - 1, a)
        return [[r, c] for (r, c) in p & a]


