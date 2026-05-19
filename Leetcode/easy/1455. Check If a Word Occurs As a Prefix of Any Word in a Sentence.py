

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # Time: O(n), n = len(sentence)
        # Space: O(n)
        def check(s: str, p: str) -> bool:
            if len(p) > len(s):
                return False
            for i in range(len(p)):
                if s[i] != p[i]:
                    return False
            return True
        s = sentence.split()
        for i, w in enumerate(s):
            if check(w, searchWord):
                return i + 1
        return -1


