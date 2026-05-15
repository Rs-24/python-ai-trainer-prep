

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        s, p = 0, 1
        while n > 0:
            s += n % 10
            p *= n % 10
            n //= 10
        return p - s


