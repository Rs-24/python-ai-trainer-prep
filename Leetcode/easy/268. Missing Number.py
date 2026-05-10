

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        out = len(nums)
        for i, num in enumerate(nums):
            out ^= (num ^ i)
        return out


