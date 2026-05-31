

class Solution:
    def countDigits(self, num: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        x = num
        c = 0
        while num > 0:
            if num % 10 != 0 and x % (num % 10) == 0:
                c += 1
            num //= 10
        return c


