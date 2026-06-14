

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        if dividend == - 2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        n = (dividend < 0) ^ (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        ans = 0
        while a >= b:
            t = b
            m = 1
            while a >= (t << 1):
                t <<= 1
                m <<= 1
            a -= t
            ans += m
        return -ans if n else ans


