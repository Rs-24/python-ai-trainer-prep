

class Solution:
    def singleNonDuplicate(self, nums: list) -> int:
        # Time: O(log n)
        # Space: O(1)
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if m % 2 != 0:
                m -= 1
            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                r = m
        return nums[l]


