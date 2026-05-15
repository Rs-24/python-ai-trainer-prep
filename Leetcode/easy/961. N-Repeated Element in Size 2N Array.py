

class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        for i in range(len(nums) - 1):
            for d in [1, 2]:
                if nums[i] == nums[i + d]:
                    return nums[i]


