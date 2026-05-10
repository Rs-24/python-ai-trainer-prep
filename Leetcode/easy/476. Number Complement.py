

class Solution:
    def findComplement(self, num: int) -> int:
        # Time: O(log num)
        # Space: O(1)
        new = 0
        while num > 0:
            new = (new << 1) | ((num & 1) ^ 1)
            num >>= 1
        return new


