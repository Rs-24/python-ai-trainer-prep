# Time to write all of below including tests, explanation and time and aux
# and total space: 9 mins

# Problem: https://leetcode.com/problems/set-mismatch/description/

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Time: O(n), n = len(nums)
        # Space, excluding output: O(n)
        seen = set()
        duplicate = None
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
        n = len(nums)
        total = (n * (n + 1)) // 2
        missing = total - sum(seen)
        return [duplicate, missing]

# Index marking version: 
from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Time: O(n), n = len(nums)
        # Space, excluding output: O(1)
        duplicate = None
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                duplicate = abs(num)
            else:
                nums[index] *= -1
        for i, num in enumerate(nums):
            if num > 0:
                return [duplicate, i + 1]
        

