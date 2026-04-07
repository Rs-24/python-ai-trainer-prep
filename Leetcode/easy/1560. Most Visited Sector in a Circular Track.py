# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/most-visited-sector-in-a-circular-track/description/

from typing import List

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        start = rounds[0]
        end = rounds[-1]
        if start <= end:
            return list(range(start, end + 1))
        return list(range(1, end + 1)) + list(range(start, n + 1))


