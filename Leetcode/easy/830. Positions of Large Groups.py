# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/positions-of-large-groups/description/

from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        # Time: O(n), n = len(s)
        # Space, excluding output: O(1)
        out = []
        l = 0
        for r, ch in enumerate(s):
            if s[l] != ch:
                if r - l >= 3:
                    out.append([l, r - 1])
                l = r
        if len(s) - l >= 3:
            out.append([l, len(s) - 1])
        return out


