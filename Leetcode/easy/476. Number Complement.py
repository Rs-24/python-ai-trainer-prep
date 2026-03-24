# Time to write all of below including tests, explanation and time and aux
# and total space: 10 mins

# Problem: https://leetcode.com/problems/number-complement/description/

class Solution:
    def findComplement(self, num: int) -> int:
        # Time: O(log n), n = num
        # Space: O(1)
        x = 0
        while num > 0:
            b = num & 1
            if b == 0:
                x |= 1
            num >>= 1
            x <<= 1
        return x >> 1

# XOR method:
class Solution:
    def findComplement(self, num: int) -> int:
        # Time: O(1)
        # Space: O(1)
        x = 1
        while x <= num:
            x <<= 1
        x -= 1
        return x ^ num

# One line XOR method
class Solution:
    def findComplement(self, num: int) -> int:
        # Time: O(1)
        # Space: O(1)
        return num ^ ((1 << num.bit_length()) - 1)


