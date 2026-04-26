# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/description/

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(n)
        rev = s[::-1]
        pairs = set()
        for i in range(len(rev) - 1):
            pairs.add(rev[i:i+2])
        for i in range(len(s) - 1):
            if s[i:i+2] in pairs:
                return True
        return False


