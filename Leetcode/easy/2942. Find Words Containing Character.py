

class Solution:
    def findWordsContaining(self, words: list, x: str) -> list:
        # Time: O(n)
        # Space: O(n)
        return [i for i, w in enumerate(words) if x in w]


