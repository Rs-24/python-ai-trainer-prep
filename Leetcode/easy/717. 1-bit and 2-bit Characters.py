# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/1-bit-and-2-bit-characters/description/

from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # Time: O(n), n = len(bits)
        # Space: O(1)
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == len(bits) - 1
        

