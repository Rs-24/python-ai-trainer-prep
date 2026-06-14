

class Solution:
    def reverse(self, x: int) -> int:
        # Time: O(log x)
        # Space: O(1)
        s = 1 if x >= 0 else -1
        m = 2 ** 31 - 1 if s else 2 ** 31
        x = abs(x)
        r = 0
        while x > 0:
            if r > (m - x % 10) // 10:
                return 0
            r = r * 10 + x % 10
            x //= 10
        return s * r


