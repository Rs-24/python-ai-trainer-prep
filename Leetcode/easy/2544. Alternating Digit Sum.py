# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/alternating-digit-sum/description/

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        # Time: O(d), d = number of digits in n
        # Space: O(d)
        sign = -1 if len(str(n)) % 2 == 0 else 1
        total = 0
        while n > 0:
            total += sign * (n % 10)
            sign *= -1
            n //= 10
        return total


