# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/shuffle-string/description/

from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Time: O(n), n = len(s)
        # Space, excluding output: O(1)
        n = len(s)
        out = [""] * n
        for i in range(n):
            out[indices[i]] = s[i]
        return "".join(out)


