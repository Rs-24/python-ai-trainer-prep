# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/description/

from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        n = len(nums)
        best = 0
        i = 0
        while i < n:
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                j = i + 1
                while j < n and nums[j] <= threshold and nums[j] % 2 != nums[j - 1] % 2:
                    j += 1
                best = max(best, j - i)
                i = j
            else:
                i += 1
        return best


