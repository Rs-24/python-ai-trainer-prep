

class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        max_num = max(nums)
        max_idx = -1
        for i, num in enumerate(nums):
            if num == max_num:
                max_idx = i
            elif num * 2 > max_num:
                return -1
        return max_idx


