# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/

class Solution:
    def makeFancyString(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Aux space: O(1)
        out = []
        for ch in s:
            if not (len(out) >= 2 and ch == out[-1] and ch == out[-2]):
                out.append(ch)
        return "".join(out)


