

from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: list) -> list:
        # Time: O(n)
        # Space: O(n)
        d = defaultdict(int)
        for p in cpdomains:
            f, x = p.split()
            t = x.split(".")
            for i in range(len(t)):
                d[".".join(t[i:])] += int(f)
        return [f"{x} {f}" for x, f in d.items()]


