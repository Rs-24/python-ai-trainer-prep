# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/license-key-formatting/description/

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Time: O(n), n = len(s)
        # Space, excluding output: O(n)
        i = len(s) - 1
        window_len = 0
        out = []
        while i >= 0:
            if s[i] != "-":
                out.append(s[i].upper())
                window_len += 1
                if window_len == k:
                    out.append("-")
                    window_len = 0
            i -= 1
        if out[-1] == "-":
            out.pop()
        return "".join(reversed(out))


        