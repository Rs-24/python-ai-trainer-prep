# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/crawler-log-folder/description/

from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # Time: O(n), n = len(logs)
        # Space: O(1)
        res = 0
        for s in logs:
            if s[0:2] == "..":
                res = max(0, res - 1)
            elif s[0].isalpha():
                res += 1
        return res


