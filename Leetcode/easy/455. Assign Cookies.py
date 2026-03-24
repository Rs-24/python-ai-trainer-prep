# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/assign-cookies/description/

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Time: O(n log n + m log m), n = len(g), m = len(s)
        # Space: O(n + m)
        g.sort(reverse=True)
        s.sort(reverse=True)
        total = 0
        i = j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                total += 1
                j += 1
            i += 1
        return total


