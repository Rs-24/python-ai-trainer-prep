# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        product = 1
        total = 0
        while n > 0:
            digit = n % 10
            product *= digit
            total += digit
            n //= 10
        return product - total


