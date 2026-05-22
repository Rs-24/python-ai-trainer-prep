

class Solution:
    def countEven(self, num: int) -> int:
        # Time: O(n log n)
        # Space: O(1)
        def even_digit_sum(x: int) -> bool:
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s % 2 == 0
        return sum(1 for i in range(1, num + 1) if even_digit_sum(i))


