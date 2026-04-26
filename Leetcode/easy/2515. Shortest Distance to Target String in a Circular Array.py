# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/description/

from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        # Time: O(n), n = len(words)
        # Space: O(1)
        best = -1
        n = len(words)
        for i, ch in enumerate(words):
            if ch == target:
                diff = abs(i - startIndex)
                d = min(diff, n - diff)
                best = d if best == -1 else min(best, d)
        return best


