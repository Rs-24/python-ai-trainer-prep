# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-minimum-log-transportation-cost/description/

class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        # Time: O(1)
        # Space: O(1)
        x = max(n, m)
        return 0 if x <= k else k * (x - k)


