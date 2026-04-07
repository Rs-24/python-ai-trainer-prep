# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/reformat-the-string/description/

class Solution:
    def reformat(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space, excluding output: O(n)
        letters = []
        digits = []
        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                digits.append(ch)
        if abs(len(letters) - len(digits)) > 1:
            return ""
        out = ["0"] * (len(letters) + len(digits))
        if len(letters) >= len(digits):
            i = 0
            for ch in letters:
                out[i] = ch
                i += 2
            i = 1
            for ch in digits:
                out[i] = ch
                i += 2
        else:
            i = 0
            for ch in digits:
                out[i] = ch
                i += 2
            i = 1
            for ch in letters:
                out[i] = ch
                i += 2
        return "".join(out)


