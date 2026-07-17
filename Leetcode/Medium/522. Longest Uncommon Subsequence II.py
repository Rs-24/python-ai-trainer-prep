

class Solution:
    def findLUSlength(self, strs: list) -> int:
        # Time: O(n^2)
        # Space: O(1)
        def c(a: str, b: str) -> bool:
            i = 0
            for ch in b:
                if i < len(a) and a[i] == ch:
                    i += 1
            return i == len(a)
        strs.sort(key=len, reverse=True)
        for i, s in enumerate(strs):
            v = True
            for j, t in enumerate(strs):
                if i == j:
                    continue
                if len(t) < len(s):
                    break
                if c(s, t):
                    v = False
                    break
            if v:
                return len(s)
        return -1


