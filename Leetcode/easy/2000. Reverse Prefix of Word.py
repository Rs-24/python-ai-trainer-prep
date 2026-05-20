

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Time: O(n), n = len(word)
        # Space: O(n)
        if ch not in word:
            return word
        return word[:word.find(ch) + 1][::-1] + word[word.find(ch) + 1:]


