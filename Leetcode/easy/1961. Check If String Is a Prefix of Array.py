

class Solution:
    def isPrefixString(self, s: str, words: list) -> bool:
        # Time: O(n), n = total number of characters in words
        # Space: O(n)
        w = ""
        for word in words:
            w += word
            if w == s:
                return True
            if len(w) > len(s):
                return False
        return False


