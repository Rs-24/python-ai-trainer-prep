# Time to write all of below including tests, explanation and time and aux
# and total space: 12 mins

# Problem: https://leetcode.com/problems/move-zeroes/description/

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        l = 0
        for r, num in enumerate(nums):
            if num != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

# insert position method: 
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        insert_pos = 0
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1


