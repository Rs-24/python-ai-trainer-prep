# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/smallest-stable-index-i/description/

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n), n = len(nums)
        l_max = nums[0]
        r_min = [0] * len(nums)
        r_min[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            r_min[i] = min(nums[i], r_min[i + 1])
        for i, num in enumerate(nums):
            l_max = max(l_max, num)
            if l_max - r_min[i] <= k:
                return i
        return -1


