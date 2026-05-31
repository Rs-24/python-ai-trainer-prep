

class Solution:
    def equalFrequency(self, word: str) -> bool:
        # Time: O(n^2)
        # Space: O(n)
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord("a")] += 1
        count = [c for c in count if c > 0]
        for i, c in enumerate(count):
            count[i] -= 1
            if len(set(x for x in count if x > 0)) == 1:
                return True
            count[i] += 1
        return False


