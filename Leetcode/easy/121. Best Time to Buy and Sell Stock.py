

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Time: O(n), n = len(prices)
        # Space: O(1)
        lowest_so_far = float("inf")
        best = 0
        for p in prices:
            best = max(best, p - lowest_so_far)
            lowest_so_far = min(lowest_so_far, p)
        return best


