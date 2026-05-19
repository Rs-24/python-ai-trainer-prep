

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # Time: O(n * k), n = len(sequence), k = maximum repetition count
        # Space: O(m * k), m = len(word)
        k = 1
        while word * k in sequence:
            k += 1
        return k - 1


