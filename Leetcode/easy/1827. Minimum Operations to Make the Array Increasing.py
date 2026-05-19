

class Solution:
    def minOperations(self, nums: list) -> int:
        # Time: O(n), n = len(nums)
        # SpaceL O(1)
        count = 0
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                diff = nums[i - 1] - nums[i] + 1
                nums[i] += diff
                count += diff
        return count


