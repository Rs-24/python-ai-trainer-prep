# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-subarrays-with-equal-sum/description/

from typing import List

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        seen = set()
        total = nums[0] + nums[1]
        seen.add(total)
        for i in range(2, len(nums)):
            total += nums[i]
            total -= nums[i - 2]
            if total in seen:
                return True
            seen.add(total)
        return False


