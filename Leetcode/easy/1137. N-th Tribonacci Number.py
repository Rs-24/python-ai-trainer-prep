

class Solution:
    def tribonacci(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        if n == 0:
            return 0
        if n <= 2:
            return 1
        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            cur = a + b + c
            a = b
            b = c
            c = cur
        return c


