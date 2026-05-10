

class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        # Time: O(n), n = len(bits)
        # Space: O(1)
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1


