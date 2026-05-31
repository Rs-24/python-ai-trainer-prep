

class Solution:
    def maximumStrongPairXor(self, nums: list) -> int:
        # Time: O(n^2)
        # Space: O(1)
        b = 0
        for x in nums:
            for y in nums:
                b = x ^ y if abs(x - y) <= min(x, y) else b
        return b


