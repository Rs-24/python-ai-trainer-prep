# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-peaks/description/

from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        # Time: O(n), n = len(mountain)
        # Aux space: O(1) 
        out = []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                out.append(i)
        return out


