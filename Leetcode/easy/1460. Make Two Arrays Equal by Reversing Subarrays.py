# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/

from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # Time: O(n log n + m log m), n = len(target), m = len(arr)
        return sorted(target) == sorted(arr)


