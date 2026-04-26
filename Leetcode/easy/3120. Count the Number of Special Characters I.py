# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-the-number-of-special-characters-i/description/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Time: O(1)
        # Space: O(1)
        s = set(word)
        count = 0
        for i in range(26):
            lower = chr(ord("a") + i)
            if lower in s and lower.upper() in s:
                count += 1
        return count


