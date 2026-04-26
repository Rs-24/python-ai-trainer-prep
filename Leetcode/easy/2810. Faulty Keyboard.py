# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/faulty-keyboard/description/

from collections import deque

class Solution:
    def finalString(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        q = deque()
        rev = False
        for ch in s:
            if ch == "i":
                rev = not rev
            else:
                if rev:
                    q.appendleft(ch)
                else:
                    q.append(ch)
        return "".join(reversed(q)) if rev else "".join(q)


