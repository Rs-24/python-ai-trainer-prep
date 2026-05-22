

class Solution:
    def minimumCost(self, cost: list) -> int:
        # Time: O(n log n)
        # Space: O(1)
        cost.sort()
        return sum(c for i, c in enumerate(cost) if i % 3 != 0)


