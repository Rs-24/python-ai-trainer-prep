# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/buy-two-chocolates/description/

from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # Time: O(n log n), n = len(prices)
        # Space: O(n)
        prices.sort()
        total = sum(prices[:2])
        ans = money - total
        return ans if ans >= 0 else money


