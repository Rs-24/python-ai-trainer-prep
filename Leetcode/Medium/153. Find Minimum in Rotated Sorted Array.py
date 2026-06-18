

class Solution:
    def findMin(self, nums: list) -> int:
        # Time: O(log n)
        # Space: O(1)
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]


        