# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/description/

from typing import List
from collections import defaultdict

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        d = defaultdict(int)
        for i, num in enumerate(nums):
            if num == key and i < len(nums) - 1:
                d[nums[i + 1]] += 1
        best = max(d.values())
        for num, freq in d.items():
            if freq == best:
                return num


