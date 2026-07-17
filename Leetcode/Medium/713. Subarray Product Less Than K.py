

class Solution:
    def numSubarrayProductLessThanK(self, nums: list, k: int) -> int:
        # Time: O(n)
        # Space: O(1)
        if k <= 1:
            return 0
        l = 0
        p = 1
        a = 0
        for r in range(len(nums)):
            p *= nums[r]
            while p >= k:
                p //= nums[l]
                l += 1
            a += r - l + 1
        return a


