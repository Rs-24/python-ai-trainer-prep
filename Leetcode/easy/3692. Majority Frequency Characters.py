

from collections import Counter, defaultdict

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        # Time: O(n)
        # Space: O(n)
        c = Counter(s)
        d = defaultdict(list)
        for ch, f in c.items():
            d[f].append(ch)
        m = max(len(v) for v in d.values())
        b_f = None
        ans = []
        for f, s in d.items():
            if len(s) == m and (b_f is None or f > b_f):
                b_f = f
                ans[:] = s
        return "".join(ans)


