

class Solution:
    def buyChoco(self, prices: list, money: int) -> int:
        # Time: O(n log n)
        # Space: O(1)
        x = money - sum(sorted(prices)[:2])
        return x if x >= 0 else money


