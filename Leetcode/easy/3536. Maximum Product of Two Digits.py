# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/maximum-product-of-two-digits/description/

class Solution:
    def maxProduct(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        first = second = 0
        while n > 0:
            d = n % 10
            if d >= first:
                second = first
                first = d
            elif d >= second:
                second = d
            n //= 10
        return first * second


