

class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        # Time: O(m * L + n), m = len(words), L = average number of letters
        # per word, n = len(order)
        # Space: O(n + L)
        d = {ch: i for i, ch in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(min(len(w1), len(w2))):
                if d[w1[j]] > d[w2[j]]:
                    return False
                if w1[j] != w2[j]:
                    break
            else:
                if len(w1) > len(w2):
                    return False
        return True


