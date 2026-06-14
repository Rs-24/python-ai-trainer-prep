

class Solution:
    def getSmallestString(self, s: str) -> str:
        # Time: O(n)
        # Space: O(n)
        s = list(s)
        for i in range(1, len(s)):
            if s[i - 1] > s[i] and int(s[i - 1]) % 2 == int(s[i]) % 2:
                s[i - 1], s[i] = s[i], s[i - 1]
                break
        return "".join(s)


