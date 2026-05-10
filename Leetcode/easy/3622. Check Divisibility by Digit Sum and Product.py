# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/description/

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        # Time: O(log n)
        # Space: O(1)
        s = 0
        p = 1
        original = n
        while n > 0:
            s += n % 10
            p *= n % 10
            n //= 10
        return original % (s + p) == 0


