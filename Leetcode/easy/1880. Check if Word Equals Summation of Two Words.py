

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        # Time: O(m + n + k), m = len(firstWord), n = len(secondWord), k = len(targetWord)
        # Space: O(1)
        def convert(s: str):
            n = 0
            for ch in s:
                n = n * 10 + ord(ch) - ord("a")
            return n
        return convert(firstWord) + convert(secondWord) == convert(targetWord)


