# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description/

class Solution:
    def kthCharacter(self, k: int) -> str:
        # Time: O(k)
        # Space: O(k)
        word = ["a"]
        while len(word) < k:
            new = []
            for ch in word:
                nxt = chr((ord(ch) - ord("a") + 1) % 26 + ord("a"))
                new.append(nxt)
            word.extend(new)
        return word[k - 1]


