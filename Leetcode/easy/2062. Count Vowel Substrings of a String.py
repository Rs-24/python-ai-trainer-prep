

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        # Time: O(n^2), n = len(word)
        # Space: O(1)
        count = 0
        v = set("aeiou")
        for i in range(len(word)):
            s = set()
            j = i
            while j < len(word) and word[j] in v:
                s.add(word[j])
                j += 1
                if len(s) == 5:
                    count += 1
        return count


