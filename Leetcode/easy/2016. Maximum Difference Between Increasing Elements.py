

class Solution:
    def maximumDifference(self, nums: list) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        min_so_far = nums[0]
        best = -1
        for i in range(1, len(nums)):
            if min_so_far < nums[i]:
                best = max(best, nums[i] - min_so_far)
            elif nums[i] < min_so_far:
                min_so_far = nums[i]
        return best


