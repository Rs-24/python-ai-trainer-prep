

class Solution:
    def pivotInteger(self, n: int) -> int:
        # Time: O(1)
        # Space: O(1)
        t = ((n + 1) * n) // 2
        x = int(t ** 0.5)
        return x if x * x == t else -1


