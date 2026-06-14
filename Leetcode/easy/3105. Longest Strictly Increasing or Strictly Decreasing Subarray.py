

class Solution:
    def longestMonotonicSubarray(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        i = d = b = 1
        for idx in range(1, len(nums)):
            if nums[idx - 1] < nums[idx]:
                i += 1
                d = 1
            elif nums[idx - 1] > nums[idx]:
                i = 1
                d += 1
            else:
                i = d = 1
            b = max(b, i, d)
        return b


