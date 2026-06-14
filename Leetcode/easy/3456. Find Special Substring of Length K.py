

class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        # Time: O(n)
        # Space: O(1)
        c = 1
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                c += 1
            else:
                if c == k:
                    start = i - k
                    l_ok = (start == 0 or s[start - 1] != s[start])
                    r_ok = (i == len(s) or s[i] != s[start])
                    if l_ok and r_ok:
                        return True
                c = 1
            if c == k:
                start = len(s) - k
                l_ok = (start == 0 or s[start - 1] != s[start])
                return l_ok
        return False


