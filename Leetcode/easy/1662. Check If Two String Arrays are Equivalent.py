

class Solution:
    def arrayStringsAreEqual(self, word1: list, word2: list) -> bool:
        # Time: O(m + n), m = total number of characters in word1, n = total
        # number of characters in word2
        # Space: O(m + n)
        return "".join(word1) == "".join(word2)


