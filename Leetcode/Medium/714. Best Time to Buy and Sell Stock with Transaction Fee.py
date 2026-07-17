

class Solution:
    def maxProfit(self, prices: list, fee: int) -> int:
        # Time: O(n)
        # Space: O(1)
        c = 0
        h = -prices[0]
        for i in range(1, len(prices)):
            t = c
            c = max(c, h + prices[i] - fee)
            h = max(h, t - prices[i])
        return c


