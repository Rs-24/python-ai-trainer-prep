

class Solution:
    def smallestRangeII(self, nums: list, k: int) -> int:
        # Time: O(n log n)
        # Space: O(1)
        nums.sort()
        n = len(nums)
        a = nums[-1] - nums[0]
        for i in range(n - 1):
            h = max(nums[-1] - k, nums[i] + k)
            l = min(nums[0] + k, nums[i + 1] - k)
            a = min(a, h - l)
        return a


        