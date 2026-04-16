# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-prefixes-of-a-given-string/description/

from typing import List

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        # Time: O(m * n), m = len(words), n = len(average word in words)
        # Space: O(1)
        count = 0
        for word in words:
            count += 1 if s.startswith(word) else 0
        return count


