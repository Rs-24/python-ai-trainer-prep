# Time to write all of below including tests, explanation and time and aux
# and total space: 18 mins

# Problem: https://leetcode.com/problems/reverse-bits/description/

class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for _ in range(32):
            out |= (n & 1)
            out <<= 1
            n >>= 1
        return out >> 1

if __name__ == "__main__":
    sol = Solution()
    assert sol.reverseBits(0) == 0
    assert sol.reverseBits(2) == 2**30
    assert sol.reverseBits(4) == 2**29
    assert sol.reverseBits(6) == 2**29 + 2**30
    assert sol.reverseBits(2**29 + 2**30) == 6
    assert sol.reverseBits(2**29) == 4
    assert sol.reverseBits(2**30) == 2

# Explanation: the code repeatedly sets the least significant bit (LSB) in out
# to the lsb in n, then shifts the bits in out left by 1, then shifts the bits
# in n right by 1. Once the loop ends it returns out with its bits shifted 
# right by 1
# Time: O(32) = O(1)
# Space: O(1)



