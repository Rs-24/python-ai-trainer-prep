# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/description/

from typing import List

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        # Time: O(n), n = len(words)
        # Space: O(1)
        if len(words) != len(s):
            return False
        for i in range(len(words)):
            if words[i][0] != s[i]:
                return False
        return True


