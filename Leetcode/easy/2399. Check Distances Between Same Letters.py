# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/check-distances-between-same-letters/description/

from typing import List

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(1)
        d = {}
        for i, ch in enumerate(s):
            if ch in d:
                if i - d[ch] - 1 != distance[ord(ch) - ord("a")]:
                    return False
            else:
                d[ch] = i
        return True


