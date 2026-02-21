# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n > 0:
            total += (n & 1)
            n >>= 1
        return total

if __name__ == "__main__":
    sol = Solution()
    assert sol.hammingWeight(1) == 1
    assert sol.hammingWeight(2) == 1
    assert sol.hammingWeight(3) == 2
    assert sol.hammingWeight(4) == 1
    assert sol.hammingWeight(11) == 3

# Explanation: the code repeatedly shifts the bits in n right by one and
# before doing so each time, adds the least significant bit in n to total
# Time: O(b), b = number of bits in n
# Space: O(1)

# Learning lessons (done after completing all of above in 7 mins):
#   - Additionally, there is also a Brian Kernighan method, my attempt is below:
#
# def hammingWeight(self, n: int) -> int:
#     # Time: O(k), k = number of 1 bits in n
#     # Space: O(1)
#     total = 0
#     while n > 0:
#         n &= (n - 1)
#         total += 1
#     return total



















































