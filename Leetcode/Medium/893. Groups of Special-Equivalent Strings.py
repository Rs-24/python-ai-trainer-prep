

class Solution:
    def numSpecialEquivGroups(self, words: list) -> int:
        # Time: O(n log n)
        # Space: O(n)
        s = set()
        for w in words:
            e, o = "".join(sorted(w[0::2])), "".join(sorted(w[1::2]))
            s.add((e, o))
        return len(s)


