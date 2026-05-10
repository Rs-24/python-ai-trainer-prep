# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description/

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        count = 0
        for i in range(len(nums) - 2):
            if (nums[i] + nums[i + 2]) * 2 == nums[i + 1]:
                count += 1
        return count


