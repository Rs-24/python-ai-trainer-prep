

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list) -> list[list]:
        d = defaultdict(list)
        for s in strs:
            c = [0] * 26
            for ch in s:
                c[ord(ch) - ord("a")] += 1
            d[tuple(c)].append(s)
        return list(d.values())


