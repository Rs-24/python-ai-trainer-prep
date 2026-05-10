# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/substring-matching-pattern/description/

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        # Time: O(m * n), m = len(s), n = len(p)
        # Space: O(1)
        i = 0
        for part in p.split("*"):
            j = s.find(part, i)
            if j == -1:
                return False
            i = j + len(part)
        return True


