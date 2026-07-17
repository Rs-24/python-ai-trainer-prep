

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # Time: O(k * (n^2))
        # Space: O(n^2)
        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0
        for _ in range(k):
            t = [[0.0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    for dr, dc in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]:
                        if 0 <= r + dr < n and 0 <= c + dc < n:
                            t[r + dr][c + dc] += dp[r][c] / 8
            dp = t
        return sum(map(sum, dp))


