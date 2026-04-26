# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/harshad-number/description/

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        # Time: O(log x)
        # Space: O(1)
        original = x
        total = 0
        while x > 0:
            total += x % 10
            x //= 10
        return total if original % total == 0 else -1


