# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/first-letter-to-appear-twice/description/

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        seen = set()
        for ch in s:
            if ch in seen:
                return ch
            seen.add(ch)


