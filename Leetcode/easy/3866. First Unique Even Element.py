# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/first-unique-even-element/description/

from typing import List
from collections import Counter

class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        c = Counter(nums)
        for num in nums:
            if num % 2 == 0 and c[num] == 1:
                return num
        return -1


