# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/delete-columns-to-make-sorted/description/

from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Time: O(m * n), m = len(strs), n = len(strs[0])
        # Space: O(1)
        total = 0
        for c in range(len(strs[0])):
            for r in range(1, len(strs)):
                if strs[r - 1][c] > strs[r][c]:
                    total += 1
                    break
        return total


