# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/description/

from typing import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        # Time: O(n^2), n = total number of characters in words
        # Space: O(n)
        built = ""
        for word in words:
            built += word
            if built == s:
                return True
            if len(built) > len(s):
                return False
        return False


