

class Solution:
    def minCosts(self, cost: list) -> list:
        # Time: O(n)
        # Space: O(n)
        out = []
        m = float("inf")
        for c in cost:
            m = min(m, c)
            out.append(m)
        return out


