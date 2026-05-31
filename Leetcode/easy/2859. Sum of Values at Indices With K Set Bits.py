

class Solution:
    def sumIndicesWithKSetBits(self, nums: list, k: int) -> int:
        # Time: O(n log n)
        # Space: O(1)
        def set_bits(x: int) -> int:
            c = 0
            while x > 0:
                x &= (x - 1)
                c += 1
            return c
        return sum(num for i, num in enumerate(nums) if set_bits(i) == k)


