# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/ugly-number/description/

class Solution:
    def isUgly(self, n: int) -> bool:
        # Time: O(log n)
        # Space: O(1)
        if n <= 0:
            return False
        for d in [2, 3, 5]:
            while n % d == 0:
                n //= d
        return n == 1


