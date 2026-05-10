# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/first-matching-character-from-both-ends/description/

class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        n = len(s)
        for i in range((n + 1) // 2):
            if s[i] == s[n - i - 1]:
                return i
        return -1


