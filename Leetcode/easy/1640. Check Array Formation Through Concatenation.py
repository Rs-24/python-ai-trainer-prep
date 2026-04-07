# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/check-array-formation-through-concatenation/description/

from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # Time: O(m + n), m = len(arr), n = len(pieces)
        # Space: O(n)
        d = {p[0]: p for p in pieces}
        i = 0
        while i < len(arr):
            if arr[i] not in d:
                return False
            p = d[arr[i]]
            for num in p:
                if i >= len(arr) or num != arr[i]:
                    return False
                i += 1
        return True


