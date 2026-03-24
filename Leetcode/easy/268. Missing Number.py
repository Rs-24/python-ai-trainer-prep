# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/missing-number/description/

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        n = len(nums)
        return ((n * (n + 1)) // 2) - sum(nums)

# XOR method:
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        x = 0
        n = len(nums)
        for i in range(1, n+1):
            x ^= (nums[i - 1] ^ i)
        return x


