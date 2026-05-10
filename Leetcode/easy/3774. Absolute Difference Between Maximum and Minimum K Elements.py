# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/description/

from typing import List

class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        # Time: O(n log n), n = len(nums)
        # Space: O(k)
        nums.sort()
        return sum(nums[-k:]) - sum(nums[:k])


