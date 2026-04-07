# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/thousand-separator/description/

class Solution:
    def thousandSeparator(self, n: int) -> str:
        # Time: O(log n)
        # Space: O(log n)
        s = str(n)
        out = []
        while len(s) > 3:
            temp = s[-3:]
            out.extend(temp[::-1])
            out.append(".")
            s = s[:-3]
        out.extend(s[::-1])
        return "".join(out[::-1])


