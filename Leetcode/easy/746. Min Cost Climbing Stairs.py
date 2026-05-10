

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # Time: O(n), n = len(cost)
        # Space: O(1)
        a = b = 0
        for i in range(2, len(cost) + 1):
            cur = min(b + cost[i - 1], a + cost[i - 2])
            a = b
            b = cur
        return b


