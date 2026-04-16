# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/reverse-prefix-of-word/description/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Time: O(n), n = len(word)
        # Aux space: O(n)
        if ch not in word:
            return word
        return word[:word.find(ch) + 1][::-1] + word[word.find(ch) + 1:]


