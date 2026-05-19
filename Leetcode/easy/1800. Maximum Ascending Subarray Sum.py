

class Solution:
    def maxAscendingSum(self, nums: list) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        best = cur = nums[0]
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                cur += nums[i + 1]
            else:
                cur = nums[i + 1]
            best = max(best, cur)
        return best


