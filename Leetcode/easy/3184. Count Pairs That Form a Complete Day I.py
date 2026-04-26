# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/description/

from typing import List
from collections import Counter

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        # Time: O(n), n = len(hours)
        # Space: O(n)
        c = Counter()
        count = 0
        for h in hours:
            h %= 24
            needed = (24 - h) % 24
            if needed in c:
                count += c[needed]
            c[h] += 1
        return count


