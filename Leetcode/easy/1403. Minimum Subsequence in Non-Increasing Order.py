

class Solution:
    def minSubsequence(self, nums: list) -> list:
        # Time: O(n log n), n = len(nums)
        # Space: O(n)
        nums.sort(reverse=True)
        r = sum(nums)
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            r -= nums[i]
            if cur > r:
                return nums[:i + 1]


