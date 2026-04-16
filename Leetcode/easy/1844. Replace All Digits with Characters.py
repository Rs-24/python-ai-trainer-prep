# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/replace-all-digits-with-characters/description/

class Solution:
    def replaceDigits(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        s = list(s)
        def shift(c: str, x: int) -> str:
            return chr(ord(c) + x)
        for i, ch in enumerate(s):
            if i % 2 != 0:
                s[i] = shift(s[i - 1], int(ch))
        return "".join(s)


