

class Solution:
    def sumZero(self, n: int) -> list:
        # Time: O(n)
        # Space: O(n)
        out = []
        for i in range(1, n // 2 + 1):
            out.append(i)
            out.append(-i)
        if n % 2 != 0:
            out.append(0)
        return out


