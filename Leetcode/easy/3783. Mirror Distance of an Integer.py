# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/mirror-distance-of-an-integer/description/

class Solution:
    def mirrorDistance(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        def reverse(x: int) -> int:
            rev = 0
            while x > 0:
                rev = rev * 10 + x % 10
                x //= 10
            return rev
        return abs(n - reverse(n))


