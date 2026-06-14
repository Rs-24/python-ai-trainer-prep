

class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        # Time: O(log n)
        # Space: O(1)
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        f = l
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m - 1
        s = l - 1
        if f <= s and f < len(nums) and nums[f] == target:
            return [f, s]
        return [-1, -1]


