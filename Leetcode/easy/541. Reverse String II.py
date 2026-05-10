

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        s = list(s)
        for i in range(0, len(s), 2 * k):
            l = i
            r = i + min(k, len(s) - i) - 1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return "".join(s)


