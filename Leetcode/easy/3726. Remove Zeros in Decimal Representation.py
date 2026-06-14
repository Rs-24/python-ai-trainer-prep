

class Solution:
    def removeZeros(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        a = 0
        p = 0
        while n > 0:
            if n % 10 != 0:
                a += (n % 10) * (10 ** p)
                p += 1
            n //= 10
        return a


