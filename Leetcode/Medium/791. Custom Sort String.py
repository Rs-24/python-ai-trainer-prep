

from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Time: O(n)
        # Space: O(n)
        c = Counter(s)
        a = []
        for ch in order:
            if ch in c.keys():
                a.append(ch * c[ch])
                del c[ch]
        for ch, f in c.items():
            a.append(ch * f)
        return "".join(a)


