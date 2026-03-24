# Time to write all of below including tests, explanation and time and aux
# and total space: 9 mins

# Problem: https://leetcode.com/problems/hamming-distance/description/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Time: O(log n), n = max(x, y)
        # Space: O(1)
        total = 0
        while x > 0 or y > 0:
            if (x & 1) != (y & 1):
                total += 1
            x >>= 1
            y >>= 1
        return total

# One-liner XOR method:
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Time: O(log n), n = max(x, y)
        # Space: O(n)
        return (x ^ y).bit_count()

# XOR counting method:
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Time: O(1)
        # Space: O(1)
        xor = x ^ y
        total = 0
        while xor > 0:
            total += (xor & 1)
            xor >>= 1
        return total


