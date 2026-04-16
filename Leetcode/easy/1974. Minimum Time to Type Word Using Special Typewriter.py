# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/description/

class Solution:
    def minTimeToType(self, word: str) -> int:
        # Time: O(n), n = len(word)
        # Aux space: O(1)
        total = 0
        for i in range(len(word)):
            cur = word[i]
            prev = word[i - 1] if i > 0 else "a"
            diff = abs(ord(cur) - ord(prev))
            total += min(diff, 26 - diff)
        return total + len(word)


