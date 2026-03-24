# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/di-string-match/description/

from typing import List 

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # Time: O(n), n = len(s)
        # Space, excluding output: O(1)
        l, r = 0, len(s)
        out = []
        for ch in s:
            if ch == "I":
                out.append(l)
                l += 1
            else:
                out.append(r)
                r -= 1
        out.append(l)
        return out


