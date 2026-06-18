

class Solution:
    def partition(self, s: str) -> list[list]:
        # Time: O(n^3)
        # Space: O(n^2)
        n = len(s)
        out = []
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        a = [(0, [])]
        while a:
            i, t = a.pop()
            if i == n:
                out.append(t)
                continue
            for e in range(n - 1, i - 1, -1):
                if is_palindrome(i, e):
                    a.append((e + 1, t + [s[i:e + 1]]))
        return out


