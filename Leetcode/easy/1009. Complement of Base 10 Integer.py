# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/complement-of-base-10-integer/description/

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        if n == 0:
            return 1
        ans = 0
        while n > 0:
            ans |= ((n & 1) ^ 1)
            n >>= 1
            ans <<= 1
        return ans >> 1


