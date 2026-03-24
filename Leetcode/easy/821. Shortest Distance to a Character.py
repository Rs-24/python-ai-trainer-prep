# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/shortest-distance-to-a-character/description/

from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # Time: O(n), n = len(s)
        # Space: O(n)
        n = len(s)
        out = [n] * n
        last_c = None
        for i, ch in enumerate(s):
            if ch == c:
                last_c = i
            if last_c is not None:
                out[i] = i - last_c
        last_c = None
        for i, ch in enumerate(s[::-1]):
            if ch == c:
                last_c = i
            if last_c is not None:
                out[n - i - 1] = min(out[n - i - 1], i - last_c)        
        return out
          

