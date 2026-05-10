# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/description/

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        x = 0
        power = 0
        total = 0
        while n > 0:
            if n % 10 != 0:
                total += n % 10
                x += (n % 10) * (10 ** power)
                power += 1
            n //= 10
        return x * total


