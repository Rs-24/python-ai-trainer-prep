

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # Time: O(n)
        # Space: O(n)
        l = nums[0]
        r = [0] * len(nums)
        r[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            r[i] = min(nums[i], r[i + 1])
        for i, x in enumerate(nums):
            l = max(l, x)
            if l - r[i] <= k:
                return i
        return -1


