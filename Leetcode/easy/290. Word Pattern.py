# Time to write all of below including tests, explanation and time and aux
# and total space: 19 mins

# Problem: https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(n)
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        p_to_s = {}
        s_to_p = {}
        for ch, word in zip(pattern, s):
            if ch not in p_to_s:
                p_to_s[ch] = word
            elif p_to_s[ch] != word:
                return False
            if word not in s_to_p:
                s_to_p[word] = ch
            elif s_to_p[word] != ch:
                return False
        return True

# Simplified version: 
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(n)
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        p_to_s = {}
        s_to_p = {}
        for ch, word in zip(pattern, s):
            if p_to_s.get(ch, word) != word or s_to_p.get(word, ch) != ch:
                return False
            p_to_s[ch] = word
            s_to_p[word] = ch
        return True


