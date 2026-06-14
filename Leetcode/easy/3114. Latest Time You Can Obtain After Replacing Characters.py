

class Solution:
    def findLatestTime(self, s: str) -> str:
        # Time: O(n)
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
                    if s[i - 1] == "0":
                        s[i] = "9"
                    else:
                        s[i] = "1"
                elif i == 3:
                    s[i] = "5"
                else:
                    s[i] = "9"
        return "".join(s)


