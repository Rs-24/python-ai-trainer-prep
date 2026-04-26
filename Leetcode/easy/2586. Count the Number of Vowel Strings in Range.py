# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/description/

from typing import List

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        # Time: O(n), n = right - left
        # Space: O(1)
        count = 0
        for i in range(left, right + 1):
            if words[i][0] in "aeiou" and words[i][-1] in "aeiou":
                count += 1
        return count


