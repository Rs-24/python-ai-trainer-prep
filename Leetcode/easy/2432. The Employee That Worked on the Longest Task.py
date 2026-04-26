# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/description/

from typing import List

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        # Time: O(k), k = len(logs)
        # Space: O(1)
        prev = 0
        ans = logs[0][0]
        best = logs[0][1]
        for a, b in logs:
            if b - prev > best:
                ans = a
                best = b - prev
            elif b - prev == best:
                ans = min(ans, a)
            prev = b
        return ans


