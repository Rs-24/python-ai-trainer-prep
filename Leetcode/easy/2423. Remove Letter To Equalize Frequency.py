# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/remove-letter-to-equalize-frequency/description/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        # Time: O(n), n = len(word)
        # Space: O(1)
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord("a")] += 1
        count = [c for c in count if c > 0]
        for i, c in enumerate(count):
            count[i] -= 1
            if len(set(c for c in count if c > 0)) == 1:
                return True
            count[i] += 1
        return False


