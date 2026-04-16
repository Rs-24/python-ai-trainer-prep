# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/counting-words-with-a-given-prefix/description/

from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # Time: O(m * n), m = len(words), n = len(pref)
        # Space: O(n)
        count = 0
        length = len(pref)
        for word in words:
            if word[:length] == pref:
                count += 1
        return count


