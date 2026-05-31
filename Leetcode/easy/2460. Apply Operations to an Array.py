

class Solution:
    def applyOperations(self, nums: list) -> list:
        # Time: O(n)
        # Space: O(1)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        l = 0
        for r, num in enumerate(nums):
            if num != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums


