# Time to write all of below including tests, explanation and time and aux 
# space: 17 mins

# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                best = max(best, profit)
        return best

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([1]) == 0
    assert sol.maxProfit([0]) == 0
    assert sol.maxProfit([1, 2]) == 1
    assert sol.maxProfit([2, 1]) == 0
    assert sol.maxProfit([0, 3, 2, 9]) == 9
    
# Explanation: The list is iterated over twice to find the max profit
# Time: O(n^2), n = len(prices)
# Aux space excluding output and input: O(1)
# Total space including output, excluding input: O(1)

# Learning lessons (done after completing all of above in 17 mins):
#   - It would have been better to do the O(n) version, my attempt is below:
#
# def maxProfit(self, prices: List[int]) -> int:
#     # Time: O(n), n = len(prices)
#     # Aux space excluding output, excluding input: O(1)
#     # Total space including output, excluding input: O(1)
#     lowest = prices[0]
#     best = 0
#     for i in range(1, len(prices)):
#         if prices[i] < lowest:
#             lowest = prices[i]
#         else:
#             best = max(best, prices[i] - lowest)
#     return best
#
#   - Additionally, it would be useful to know the Kadane's algorithm version,
#     my attempt is below:
#
# def maxProfit(self, prices: List[int]) -> int:
#     # Time: O(n), n = len(prices)
#     # Aux space excluding output and input: O(1)
#     # Total space excluding output, including input: O(1)
#     current, best = 0, 0
#     for i in range(1, len(prices)):
#         diff = prices[i] - prices[i-1]
#         current = max(0, current + diff)
#         best = max(best, current)
#     return best



    






        
        

            
            


