

class Solution:
    def findAndReplacePattern(self, words: list, pattern: str) -> list:
        # Time: O(n)
        # Space: O(n)
        def c(s: str):
            p_s = {}
            s_p = {}
            for a, b in zip(pattern, s):
                if a in p_s:
                    if p_s[a] != b:
                        return False
                else:
                    p_s[a] = b
                if b in s_p:
                    if s_p[b] != a:
                        return False
                else:
                    s_p[b] = a
            return True
        return [w for w in words if c(w)]


        