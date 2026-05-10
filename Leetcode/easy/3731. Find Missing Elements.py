# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-missing-elements/description/

from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # Time: O(n + max(nums) - min(nums)), n = len(nums)
        # Space: O(n)
        l, h = min(nums), max(nums)
        s = set(nums)
        return [x for x in range(l + 1, h) if x not in s]


