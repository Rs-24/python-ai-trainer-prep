# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/base-7/description/

class Solution:
    def convertToBase7(self, num: int) -> str:
        # Time: O(log n), n = num
        # Space, excluding output: O(log n)
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        digits = []
        while num > 0:
            digits.append(str(num % 7))
            num //= 7
        if negative:
            digits.append("-")
        return "".join(reversed(digits))


