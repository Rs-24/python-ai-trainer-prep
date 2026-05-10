# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/count-dominant-indices/description/

from typing import List

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        n = len(nums)
        if n <= 1:
            return 0
        suffix_sum = nums[-1]
        count = 0
        for i in range(n - 2, -1, -1):
            r_len =  n - i - 1
            if nums[i] * r_len > suffix_sum:
                count += 1
            suffix_sum += nums[i]
        return count


