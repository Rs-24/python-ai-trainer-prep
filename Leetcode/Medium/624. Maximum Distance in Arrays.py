

class Solution:
    def maxDistance(self, arrays: list[list]) -> int:
        # Time: O(n)
        # Space: O(1)
        gmi, gma, a = float("inf"), float("-inf"), float("-inf")
        for p in arrays:
            a = max(a, p[-1] - gmi, gma - p[0])
            gmi = min(gmi, p[0])
            gma = max(gma, p[-1])
        return a


