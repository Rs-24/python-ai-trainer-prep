

class Solution:
    def specialArray(self, nums: list) -> int:
        # Time: O(n log n), n = len(nums)
        # Space: O(1)
        n = len(nums)
        nums.sort()
        for i in range(1, n + 1):
            if nums[n - i] >= i and (i == n or nums[n - i - 1] < i):
                return i
        return -1


