

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Time: O(log n)
        # Space: O(1)
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1


