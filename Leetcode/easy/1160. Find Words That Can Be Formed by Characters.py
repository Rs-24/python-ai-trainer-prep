

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        # Time: O(m + n), m = total number of characters in words, n = len(chars)
        # Space: O(1)
        c = [0] * 26
        for ch in chars:
            c[ord(ch) - ord("a")] += 1
        total = 0
        for word in words:
            temp = c.copy()
            for ch in word:
                temp[ord(ch) - ord("a")] -= 1
            if all(t >= 0 for t in temp):
                total += len(word)
        return total


