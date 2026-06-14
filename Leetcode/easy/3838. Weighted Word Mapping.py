

class Solution:
    def mapWordWeights(self, words: list, weights: list) -> str:
        # Time: O(n)
        # Space: O(n)
        return "".join(
            chr(ord("z") - (sum(weights[ord(ch) - ord("a")] for ch in w) % 26))
            for w in words)


