# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/reverse-string/description/

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # Time: O(n), n = len(s)
        # Space: O(1)
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


