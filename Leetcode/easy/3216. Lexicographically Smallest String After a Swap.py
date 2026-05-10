# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/description/

class Solution:
    def getSmallestString(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        s = list(s)
        for i in range(1, len(s)):
            if s[i - 1] > s[i] and int(s[i - 1]) % 2 == int(s[i]) % 2:
                s[i - 1], s[i] = s[i], s[i - 1]
                break
        return "".join(s)


