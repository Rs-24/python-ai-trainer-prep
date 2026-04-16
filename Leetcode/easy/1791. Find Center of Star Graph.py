# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/find-center-of-star-graph/description/

from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Time: O(1)
        # Space: O(1)
        a, b = edges[0]
        c, d = edges[1]
        if a == c or a == d:
            return a
        return b

