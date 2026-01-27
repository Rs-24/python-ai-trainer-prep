# Time to write all of below including tests, explanation and time and aux
# and total space: 38 mins

# Problem: https://leetcode.com/problems/reverse-bits/description/

class Solution:
    def reverseBits(self, n: int) -> int:
        power = 30
        binary = []
        total = n
        while power >= 0:
            if total - 2**power >= 0:
                binary.append(1)
                total -= 2**power
            else:
                binary.append(0)
            power -= 1
        binary.append(0)
        binary.reverse()
        new_total = 0
        for i, d in enumerate(binary[1:]):
            new_total += d * (2 ** i)
        return new_total

if __name__ == "__main__":
    sol = Solution()
    assert sol.reverseBits(0) == 0
    assert sol.reverseBits(2) == 2**29
    assert sol.reverseBits(4) == 2**28
    assert sol.reverseBits(2**29) == 2
    assert sol.reverseBits(2**28) == 4
    assert sol.reverseBits(443261596) == 964176192
    assert sol.reverseBits(2147483644) == 1073741822

# Explanation: first n is converted to binary and reversed, then the value
# corresponding to the new binary number is returned
# Time: O(n)
# Aux space, excluding output and input: O(n)
# Total space, including output, excluding input: O(n)

# Learning lessons (done after completing all of above in 38 mins):
#   - I now realise my solution is wrong. My rewrite is below:
#
# def reverseBits(self, n: int) -> int:
#     # Time: O(1)
#     # Aux space, excluding output and input: O(1)
#     # Total space, including output, excluding input: O(1)
#     res = 0
#     for _ in range(32):
#         res = (res << 1) | (n & 1)
#         n >>= 1
#     return res
#
#   - Additionally, my tests could have been corrected and simplified. My new
#     tests are below:
#
# if __name__ == "__main__":
#     sol = Solution()
#     assert sol.reverseBits(0) == 0
#     assert sol.reverseBits(2) == 2**30
#     assert sol.reverseBits(4) == 2**29
#     assert sol.reverseBits(2**30) == 2
#     assert sol.reverseBits(2**29) == 4
    



















