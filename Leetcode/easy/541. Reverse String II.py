# Time to write all of below including tests, explanation and time and aux
# and total space: 12 mins

# Problem: https://leetcode.com/problems/reverse-string-ii/description/

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Time: O(n + k), n = len(s)
        # Space, excluding output: O(n + k)
        chars = list(s)
        i = 0
        while i < len(s):
            chars[i:i + k] = chars[i:i + k][::-1]
            i += (2 * k)
        return "".join(chars)

# Modifying in-place version:
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Time: O(n), n = len(s)
        # Space, excluding output: O(n)
        s = list(s)
        i = 0
        while i < len(s):
            l = i
            r = i + min(k, len(s) - i) - 1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            i += (2 * k)
        return "".join(s)


