

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Time: O(n), n = len(s) = len(t)
        # Space: O(n)
        s_to_t = {}
        t_to_s = {}
        for ch1, ch2 in zip(s, t):
            if ch1 not in s_to_t:
                s_to_t[ch1] = ch2
            if ch2 not in t_to_s:
                t_to_s[ch2] = ch1
            if s_to_t[ch1] != ch2 or t_to_s[ch2] != ch1:
                return False
        return True


