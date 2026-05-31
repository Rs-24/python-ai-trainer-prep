

class Solution:
    def maximumCount(self, nums: list) -> int:
        # Time: O(log n)
        # Space: O(1)
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < 0:
                l = mid + 1
            else:
                r = mid
        n = l
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= 0:
                l = mid + 1
            else:
                r = mid
        p = len(nums) - l
        return max(n, p)


