# Time to write all of below including tests, explanation and time and aux
# and total space: 9 mins

# Problem: https://leetcode.com/problems/backspace-string-compare/description/

from typing import List

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Time: O(m + n), m = len(s), n = len(t)
        # Space: O(m + n)
        def build(string: str) -> List[str]:
            out = []
            for ch in string:
                if ch == "#":
                    if out != []:
                        out.pop()
                else:
                    out.append(ch)
            return out
        return build(s) == build(t)

# O(1) space version:
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Time: O(m + n), m = len(s), n = len(t)
        # Space: O(1)
        i, j = len(s) - 1, len(t) - 1
        skip_s = skip_t = 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == "#":
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if s[j] == "#":
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        return True


