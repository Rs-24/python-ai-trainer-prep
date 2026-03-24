# Time to write all of below including tests, explanation and time and aux
# and total space: 6 mins

# Problem: https://leetcode.com/problems/longest-harmonious-subsequence/description/

from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(k), k = number of unique values, worst case O(n)
        c = Counter(nums)
        best = 0
        for num, freq in c.items():
            if num + 1 in c:
                best = max(best, freq + c[num + 1])
        return best


