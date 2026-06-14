

class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        # Time: O(1)
        # Space: O(1)
        return 0 if max(n, m) <= k else k * (max(n, m) - k)


