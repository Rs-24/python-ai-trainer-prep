

class Solution:
    def myAtoi(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        sign = -1 if i < len(s) and s[i] == "-" else 1
        i += s[i] in "+-"
        n = 0
        m = 2 ** 31 - 1 if sign == 1 else 2 ** 31
        while i < len(s) and s[i].isdigit():
            if n > (m - ord(s[i]) - ord("0")) // 10:
                return sign * m
            n = n * 10 + ord(s[i]) - ord("0")
            i += 1
        return sign * n


