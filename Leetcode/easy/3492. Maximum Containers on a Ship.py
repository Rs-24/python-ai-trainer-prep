

class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        # Time: O(1)
        # Space: O(1)
        return min(n * n, maxWeight // w)


