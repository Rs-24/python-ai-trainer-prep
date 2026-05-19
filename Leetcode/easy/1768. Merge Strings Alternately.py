

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Time: O(m + n), m = len(word1), n = len(word2)
        # Space: O(m + n)
        out = []
        i = j = 0
        while i < len(word1) and j < len(word2):
            out.append(word1[i])
            out.append(word2[j])
            i += 1
            j += 1
        out.append(word1[i:])
        out.append(word2[j:])
        return "".join(out)


