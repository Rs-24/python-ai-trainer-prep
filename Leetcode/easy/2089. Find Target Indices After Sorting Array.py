# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Time: O(n), n = len(nums)
        # Aux space: O(1)
        less = 0
        same = 0
        for num in nums:
            less += 1 if num < target else 0
            same += 1 if num == target else 0
        return [i for i in range(less, less + same)]


