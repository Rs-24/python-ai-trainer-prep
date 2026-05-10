

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Time: O(m + n), m = len(s), n = len(t)
        # Space: O(1)
        def nxt(string: str, idx: int) -> int:
            skip = 0
            while idx >= 0:
                if string[idx] == "#":
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    break
                idx -= 1
            return idx
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            i = nxt(s, i)
            j = nxt(t, j)
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        return True


