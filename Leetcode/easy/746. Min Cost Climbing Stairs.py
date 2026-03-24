# Time to write all of below including tests, explanation and time and aux
# and total space: 10 mins

# Problem: https://leetcode.com/problems/min-cost-climbing-stairs/description/

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Time: O(n), n = len(cost)
        # Space: O(1)
        prev_prev = prev = 0
        for i in range(2, len(cost) + 1):
            cur = min(prev_prev + cost[i - 2], prev + cost[i - 1])
            prev_prev = prev
            prev = cur
        return cur

# Dynamic programming version:
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Time: O(n), n = len(cost)
        # Space: O(n)
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[len(cost)]


