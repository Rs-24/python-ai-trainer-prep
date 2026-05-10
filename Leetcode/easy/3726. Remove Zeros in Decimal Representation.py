# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/remove-zeros-in-decimal-representation/description/

class Solution:
    def removeZeros(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        new = 0
        power = 0
        while n > 0:
            if n % 10 != 0:
                new += (n % 10) * (10 ** power)
                power += 1
            n //= 10
        return new


