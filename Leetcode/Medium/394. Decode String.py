

class Solution:
    def decodeString(self, s: str) -> str:
        # Time: O(n)
        # Space: O(n)
        out = []
        t = []
        x = 0
        for ch in s:
            if ch.isdigit():
                x = x * 10 + int(ch)
            elif ch == "[":
                t.append((out, x))
                out = []
                x = 0
            elif ch == "]":
                p, y = t.pop()
                out = p + out * y
            else:
                out.append(ch)
        return "".join(out)


