

from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list]) -> list[list]:
        # Time: O(m * n)
        # Space: O(m * n)
        m, n = len(mat), len(mat[0])
        a = [[-1] * n for _ in range(m)]
        q = deque()
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    a[r][c] = 0
                    q.append((r, c))
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.popleft()
            for dr, dc in d:
                if (0 <= r + dr < m and 0 <= c + dc < n and a[r + dr][c + dc] == -1):
                    a[r + dr][c + dc] = a[r][c] + 1
                    q.append((r + dr, c + dc))
        return a


