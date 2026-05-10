

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        out = 0
        for num in nums:
            out ^= num
        return out


