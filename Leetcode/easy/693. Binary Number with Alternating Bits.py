# Time to write all of below including tests, explanation and time and aux
# and total space: 6 mins

# Problem: https://leetcode.com/problems/binary-number-with-alternating-bits/description/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Time: O(log n)
        # Space: O(1)
        prev = None
        while n > 0:
            if prev is not None and prev ^ (n & 1) == 0:
                return False
            prev = n & 1
            n >>= 1
        return True

# Simpler version:
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        x = n ^ (n >> 1)
        return x & (x + 1) == 0


