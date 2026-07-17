

class Solution:
    def change(self, amount: int, coins: list) -> int:
        # Time: O(amount * len(coins))
        # Space: O(amount)
        dp = [1] + [0] * amount
        for c in coins:
            for x in range(c, amount + 1):
                dp[x] += dp[x - c]
        return dp[amount]


