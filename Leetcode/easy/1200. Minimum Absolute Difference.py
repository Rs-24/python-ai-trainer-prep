# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/minimum-absolute-difference/description/

from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Time: O(n log n), n = len(arr)
        # Space, excluding output: O(n)
        arr.sort()
        best = float("inf")
        for i in range(1, len(arr)):
            best = min(best, arr[i] - arr[i - 1])
        out = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == best:
                out.append([arr[i - 1], arr[i]])
        return out


