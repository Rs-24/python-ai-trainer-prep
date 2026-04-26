# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/description/

class Solution:
    def findLatestTime(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        s = list(s)
        for i, ch in enumerate(s):
            if ch == "?":
                if i == 0:
                    if s[i + 1] == "?" or int(s[i + 1]) <= 1:
                        s[i] = "1"
                    else:
                        s[i] = "0"
                elif i == 1:
                    if s[i - 1] == "1":
                        s[i] = "1"
                    else:
                        s[i] = "9"
                elif i == 3:
                    s[i] = "5"
                else:
                    s[i] = "9"
        return "".join(s)


