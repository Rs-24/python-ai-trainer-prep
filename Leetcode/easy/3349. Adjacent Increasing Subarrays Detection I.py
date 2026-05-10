# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/description/

from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        cur = 1
        prev = 0
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                cur += 1
            else:
                prev = cur
                cur = 1
            if (prev >= k and cur >= k) or cur >= 2 * k:
                return True
        return False


