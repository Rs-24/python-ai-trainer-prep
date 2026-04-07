# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/rank-transform-of-an-array/description/

from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Time: O(n log n), n = len(arr)
        # Space: O(n)
        d = {}
        for i, num in enumerate(sorted(set(arr)), 1):
            d[num] = i
        return [d[num] for num in arr]


