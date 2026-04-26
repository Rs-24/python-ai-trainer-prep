# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/description/

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Time: O(n), n = len(word)
        # Space: O(1)
        total = 0
        i = 0
        while i < len(word):
            total += (i // 8) + 1
            i += 1
        return total


