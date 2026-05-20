

from collections import Counter

class Solution:
    def countWords(self, words1: list, words2: list) -> int:
        # Time: O(m + n), m = len(words1), n = len(words2)
        # Space: O(m + n)
        c1 = Counter(words1)
        c2 = Counter(words2)
        return sum(1 for word, freq in c1.items() if freq == 1 and c2[word] == 1)


