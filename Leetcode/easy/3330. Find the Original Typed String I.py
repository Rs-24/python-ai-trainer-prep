# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-original-typed-string-i/description/

class Solution:
    def possibleStringCount(self, word: str) -> int:
        # Time: O(n), n = len(word)
        # Space: O(1)
        res = 1
        for i in range(1, len(word)):
            if word[i - 1] == word[i]:
                res += 1
        return res


