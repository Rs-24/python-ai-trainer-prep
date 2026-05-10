# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/valid-digit-number/description/

class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        # Time: O(log n)
        # Space: O(1)
        last_digit = None
        x_in_n = False
        while n > 0:
            digit = n % 10
            if digit == x:
                x_in_n = True
            last_digit = digit
            n //= 10
        return last_digit != x and x_in_n


