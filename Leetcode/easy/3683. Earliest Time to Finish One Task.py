

class Solution:
    def earliestTime(self, tasks: list[list]) -> int:
        # Time: O(n)
        # Space: O(1)
        return min(a + b for a, b in tasks)


