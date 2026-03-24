# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/power-of-three/description/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Time: O(log n)
        # Space: O(1)
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1


