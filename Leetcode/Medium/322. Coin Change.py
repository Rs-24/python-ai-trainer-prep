

class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        # Time: O(len(amount) * len(coins))
        # Space: O(len(amount))
        dp = [0] + [float("inf")] * amount
        for x in range(1, amount + 1):
            for c in coins:
                if x - c >= 0:
                    dp[x] = min(dp[x], dp[x - c] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1


