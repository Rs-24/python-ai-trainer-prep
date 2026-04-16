# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Time: O(1)
        # Space: O(1)
        return (start ^ goal).bit_count()


