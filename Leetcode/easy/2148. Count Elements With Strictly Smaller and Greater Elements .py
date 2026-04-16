# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/description/

from typing import List

class Solution:
    def countElements(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        l, h = min(nums), max(nums)
        count = 0
        for num in nums:
            if num > l and num < h:
                count += 1
        return count


