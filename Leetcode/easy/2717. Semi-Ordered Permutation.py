# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/semi-ordered-permutation/description/

from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        n = len(nums)
        i, j = nums.index(1), nums.index(n)
        return i + n - 1 - j - (i > j)


