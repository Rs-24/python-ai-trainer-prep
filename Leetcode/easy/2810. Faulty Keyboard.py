

from collections import deque

class Solution:
    def finalString(self, s: str) -> str:
        # Time: O(n)
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


