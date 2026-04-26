# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/description/

from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        n = len(nums)
        prefix_max = [nums[0]]
        for num in nums[1:]:
            prefix_max.append(max(prefix_max[-1], num))
        suffix_max = [nums[-1]]
        for num in nums[::-1][:-1]:
            suffix_max.append(max(suffix_max[-1], num))
        suffix_max.reverse()
        best = 0
        for j in range(1, len(nums) - 1):
            best = max(best, (prefix_max[j - 1] - nums[j]) * suffix_max[j + 1])
        return best


