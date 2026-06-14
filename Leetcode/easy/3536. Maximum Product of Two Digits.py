

class Solution:
    def maxProduct(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        f = s = 0
        while n > 0:
            if n % 10 >= f:
                s = f
                f = n % 10
            elif n % 10 >= s:
                s = n % 10
            n //= 10
        return f * s


