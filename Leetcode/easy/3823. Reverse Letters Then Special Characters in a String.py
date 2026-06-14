

class Solution:
    def reverseByType(self, s: str) -> str:
        # Time: O(n)
        # Space: O(n)
        l, sp = [], []
        for ch in s:
            if ch.isalpha():
                l.append(ch)
            else:
                sp.append(ch)
        l.reverse()
        sp.reverse()
        out = []
        i = j = 0
        for ch in s:
            if ch.isalpha():
                out.append(l[i])
                i += 1
            else:
                out.append(sp[j])
                j += 1
        return "".join(out)


