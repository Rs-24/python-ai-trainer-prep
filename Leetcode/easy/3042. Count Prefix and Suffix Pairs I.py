

class Solution:
    def countPrefixSuffixPairs(self, words: list) -> int:
        # Time: O(n^2)
        # Space: O(1)
        c = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    c += 1
        return c


