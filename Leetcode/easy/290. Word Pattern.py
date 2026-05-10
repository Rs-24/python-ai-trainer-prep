

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Time: O(m + n), m = len(pattern), n = len(s)
        # Space: O(m + n)
        s = s.split()
        if len(pattern) != len(s):
            return False
        p_to_s = {}
        s_to_p = {}
        for ch, word in zip(pattern, s):
            if ch in p_to_s:
                if p_to_s[ch] != word:
                    return False
            else:
                p_to_s[ch] = word
            if word in s_to_p:
                if s_to_p[word] != ch:
                    return False
            else:
                s_to_p[word] = ch
        return True


