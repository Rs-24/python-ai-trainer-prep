# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/intersection-of-multiple-arrays/description/

from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        # Time: O(n + k log k), n = total number of numbers in nums, k = len(out)
        # Aux space: O(n + k)
        sets = []
        for arr in nums:
            sets.append(set(arr))
        out = sets[0]
        for s in sets[1:]:
            out &= s
        return sorted(list(out))


