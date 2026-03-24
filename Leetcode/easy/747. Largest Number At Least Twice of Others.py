# Time to write all of below including tests, explanation and time and aux
# and total space: 11 mins

# Problem: https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/

from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        max_num = max(nums)
        max_index = nums.index(max_num)
        for num in nums:
            if num != max_num and 2 * num > max_num:
                return -1
        return max_index

# Alternative version:
from typing import List
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        max_num = 0
        next_max = 0
        max_index = 0
        for i, num in enumerate(nums):
            if num > max_num:
                next_max = max_num
                max_num = num
                max_index = i
            elif num > next_max:
                next_max = num
        return -1 if 2 * next_max > max_num else max_index


