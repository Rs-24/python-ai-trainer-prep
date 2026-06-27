

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        if n == 0:
            return 1
        n = min(n, 10)
        t = 10
        u = 9
        d = 9
        for i in range(2, n + 1):
            u *= d
            t += u
            d -= 1
        return t


