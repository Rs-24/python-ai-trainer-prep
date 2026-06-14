

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # Time: O(n log n)
        # Space: O(1)
        def digit_product(x: int) -> int:
            p = 1
            while x > 0:
                p *= x % 10
                x //= 10
            return p
        while digit_product(n) % t != 0:
            n += 1
        return n


