# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-maximum-number-of-string-pairs/description/

from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # Time: O(n), n = total number of characters in words
        # Space: O(n)
        seen = set()
        count = 0
        for word in words:
            if word[::-1] in seen:
                count += 1
            else:
                seen.add(word)
        return count


