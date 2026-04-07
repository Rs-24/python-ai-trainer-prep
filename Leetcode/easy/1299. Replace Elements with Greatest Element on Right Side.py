# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/

from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Time: O(n), n = len(arr)
        # Space: O(1)
        best = -1
        i = len(arr) - 1
        while i >= 0:
            temp = arr[i]
            arr[i] = best
            best = max(best, temp)
            i -= 1
        return arr


