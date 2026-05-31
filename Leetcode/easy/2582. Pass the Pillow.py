

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # Time: O(1)
        # Space: O(1)
        c = 2 * (n - 1)
        p = time % c
        return p + 1 if p < n - 1 else n - (p - (n - 1))


