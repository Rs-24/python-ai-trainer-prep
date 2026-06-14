

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        # Time: O(1)
        # Space: O(1)
        c = 2 * (n - 1)
        p = k % c
        return p if p <= n - 1 else c - p


