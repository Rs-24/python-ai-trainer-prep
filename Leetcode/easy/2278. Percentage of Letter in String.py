# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/percentage-of-letter-in-string/description/

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        return int((100 * s.count(letter)) // len(s))


