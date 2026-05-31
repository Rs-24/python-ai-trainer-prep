

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        s = 1 if len(str(n)) % 2 != 0 else -1
        t = 0
        while n > 0:
            t += s * (n % 10)
            s *= -1
            n //= 10
        return t


