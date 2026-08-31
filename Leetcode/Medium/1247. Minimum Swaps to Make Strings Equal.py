

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # Time: O(n)
        # Space: O(1)
        xy = yx = 0
        for a, b in zip(s1, s2):
            xy += (a == "x" and b == "y")
            yx += (a == "y" and b == "x")
        if (xy + yx) % 2:
            return -1
        return xy // 2 + yx // 2 + 2 * (xy % 2)


