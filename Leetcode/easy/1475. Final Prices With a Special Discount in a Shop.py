

class Solution:
    def finalPrices(self, prices: list) -> list:
        # Time: O(n), n = len(prices)
        # Space: O(n)
        s = []
        for i, p in enumerate(prices):
            while s and prices[s[-1]] >= p:
                j = s.pop()
                prices[j] -= p
            s.append(i)
        return prices


