

class Solution:
    def countPartitions(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        l = 0
        r = sum(nums)
        c = 0
        for i in range(len(nums) - 1):
            l += nums[i]
            r -= nums[i]
            c += abs(l - r) % 2 == 0
        return c


