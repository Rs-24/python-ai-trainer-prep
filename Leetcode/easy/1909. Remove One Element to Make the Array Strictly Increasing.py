

class Solution:
    def canBeIncreasing(self, nums: list) -> bool:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        removed = 0
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                removed += 1
                if i > 1 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]
        return removed <= 1


