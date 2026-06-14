

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        # Time: O(n)
        # Space: O(1)
        c = [0, 0]
        l = t = 0
        for r in range(len(s)):
            c[int(s[r])] += 1
            while c[0] > k and c[1] > k:
                c[int(s[l])] -= 1
                l += 1
            t += r - l + 1
        return t


