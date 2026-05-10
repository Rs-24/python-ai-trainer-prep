

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        l = 0
        for r, num in enumerate(nums):
            if num != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1


