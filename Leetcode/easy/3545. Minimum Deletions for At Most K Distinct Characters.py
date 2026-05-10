# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/description/

from collections import Counter

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        c = Counter(s)
        if len(c) <= k:
            return 0
        counts = sorted(c.values())
        remove = len(counts) - k
        return sum(counts[:remove])


