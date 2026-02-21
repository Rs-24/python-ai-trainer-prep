# Time to write all of below including tests, explanation and time and aux 
# space: 17 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

from typing import List 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        best = 0
        for price in prices[1:]:
            best = max(best, price - lowest)
            lowest = min(lowest, price)
        return best

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([1]) == 0
    assert sol.maxProfit([1, 2]) == 1
    assert sol.maxProfit([2, 1]) == 0
    assert sol.maxProfit([5, 4, 3, 2, 1]) == 0
    assert sol.maxProfit([2, 2, 1, 1, 1]) == 0
    assert sol.maxProfit([0, 6, 2, 8]) == 8
    assert sol.maxProfit([1, 4, 2, 3, 1]) == 3
    
# Explanation: the code uses two variables: lowest and best, and iterates
# through the list while continuously updating best and lowest using the
# current price
# Time: O(n), n = len(prices)
# Space: O(1)

# Learning lessons (done after completing all of above in 17 mins):
#   - Additionally, it would be useful to know the Kadane's algorithm version,
#     my attempt is below:
#
# def maxProfit(self, prices: List[int]) -> int:
#     # Time: O(n), n = len(prices)
#     # Space: O(1)
#     current = 0
#     best = 0
#     for i in range(1, len(prices)):
#         diff = prices[i] - prices[i - 1]
#         current = max(0, current + diff)
#         best = max(best, current)
#     return best


            


