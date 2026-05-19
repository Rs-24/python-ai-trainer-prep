

class Solution:
    def modifyString(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        out = []
        for i, ch in enumerate(s):
            if ch == "?":
                prev = None if len(out) == 0 else out[-1]
                nxt = None if i == len(s) - 1 else s[i + 1]
                for new in ["a", "b", "c"]:
                    if new != prev and new != nxt:
                        ch = new
                        break
            out.append(ch)
        return "".join(out)


