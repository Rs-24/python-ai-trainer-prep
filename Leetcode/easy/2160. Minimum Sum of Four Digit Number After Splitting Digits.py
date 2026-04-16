# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/

class Solution:
    def minimumSum(self, num: int) -> int:
        # Time: O(n log n), n = len(str(num))
        # Space: O(n)
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10
        digits.sort()
        num1 = digits[0] * 10 + digits[2]
        num2 = digits[1] * 10 + digits[3]
        return num1 + num2


