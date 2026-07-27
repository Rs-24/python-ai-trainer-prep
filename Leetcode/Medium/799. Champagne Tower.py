

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Time: O(n^2)
        # Space: O(n^2)
        dp = [[0.0] * (r + 1) for r in range(query_row + 2)]
        dp[0][0] = float(poured)
        for r in range(query_row + 1):
            for c in range(r + 1):
                t = max(0.0, dp[r][c] - 1.0)
                if t > 0:
                    dp[r + 1][c] += t / 2
                    dp[r + 1][c + 1] += t / 2
        return min(1.0, dp[query_row][query_glass])


