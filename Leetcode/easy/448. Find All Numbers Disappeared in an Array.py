# Time to write all of below including tests, explanation and time and aux
# and total space: 12 mins

# Problem: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Time: O(n), n = len(nums)
        # Space, excluding output: O(1)
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        out = []
        for i, num in enumerate(nums):
            if num > 0:
                out.append(i + 1)
        return out

# set method:
from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Time: O(n), n = len(nums)
        # Space, excluding output: O(n)
        return [i for i in range(1, len(nums) + 1) if i not in set(nums)]


