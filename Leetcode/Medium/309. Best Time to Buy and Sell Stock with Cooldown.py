

class Solution:
    def maxProfit(self, prices: list) -> int:
        # Time: O(n)
        # Space: O(1)
        h, s, r = -prices[0], 0, 0
        for i in range(1, len(prices)):
            hp, sp, rp = h, s, r
            h = max(hp, rp - prices[i])
            s = hp + prices[i]
            r = max(rp, sp)
        return max(s, r)


