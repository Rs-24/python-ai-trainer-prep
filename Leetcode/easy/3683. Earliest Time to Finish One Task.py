# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/earliest-time-to-finish-one-task/description/

from typing import List

class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        # Time: O(n), n = len(tasks)
        # Space: O(1)
        best = float("inf")
        for a, b in tasks:
            best = min(best, a + b)
        return best


