# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/

from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Time: O(n), n = len(prices)
        # Space: O(n)
        stack = []
        for i, p in enumerate(prices):
            while len(stack) > 0 and prices[stack[-1]] >= p:
                j = stack.pop()
                prices[j] -= p
            stack.append(i)
        return prices


