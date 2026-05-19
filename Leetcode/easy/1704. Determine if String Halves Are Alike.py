

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(1)
        n = len(s)
        t1 = t2 = 0
        for i, ch in enumerate(s):
            if ch in "aeiouAEIOU":
                if i < n // 2:
                    t1 += 1
                else:
                    t2 += 1
        return t1 == t2


