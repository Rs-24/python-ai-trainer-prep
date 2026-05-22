

class Solution:
    def mostWordsFound(self, sentences: list) -> int:
        # Time: O(n)
        # Space: O(n)
        return max(len(s.split()) for s in sentences)


