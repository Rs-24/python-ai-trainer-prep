# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/

from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # Time: O(n * m), n = len(words), m = average length of a word in
        # words
        # Space: O(m)
        for word in words:
            if word == word[::-1]:
                return word
        return ""


