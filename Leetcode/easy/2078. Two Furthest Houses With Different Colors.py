

class Solution:
    def maxDistance(self, colors: list) -> int:
        # Time: O(n), n = len(colors)
        # Space: O(1)
        best = 0
        for i, c in enumerate(colors):
            if c != colors[0]:
                best = max(best, i)
            if c != colors[-1]:
                best = max(best, len(colors) - i - 1)
        return best


