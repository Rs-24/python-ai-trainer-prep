

class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        # Time: O(log n)
        # Space: O(1)
        l = 0
        v = False
        while n > 0:
            l = n % 10
            if l == x:
                v = True
            n //= 10
        return l != x and v


