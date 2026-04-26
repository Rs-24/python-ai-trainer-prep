# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/split-strings-by-separator/description/

from typing import List

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        # Time: O(n), n = total number of characters in words
        # Space: O(n) 
        out = []
        for word in words:
            parts = word.split(separator)
            for part in parts:
                if part:
                    out.append(part)
        return out


