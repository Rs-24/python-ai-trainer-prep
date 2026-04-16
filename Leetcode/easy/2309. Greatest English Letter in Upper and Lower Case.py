# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/description/

class Solution:
    def greatestLetter(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        s = set(s)
        for i in range(ord("Z"), ord("A") - 1, -1):
            if chr(i) in s and chr(i).lower() in s:
                return chr(i)
        return ""


