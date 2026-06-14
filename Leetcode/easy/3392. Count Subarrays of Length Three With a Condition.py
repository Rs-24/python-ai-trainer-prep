

class Solution:
    def countSubarrays(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        return sum(1 for i in range(len(nums) - 2) if 2 * (nums[i] + nums[i + 2]) == nums[i + 1])


