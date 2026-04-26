# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/description/

from typing import List

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        # Time: O(n), n = total number of characters in strs
        # Space: O(1)
        best = 0
        for s in strs:
            cur = int(s) if all(ch.isdigit() for ch in s) else len(s)
            best = max(best, cur)
        return best


