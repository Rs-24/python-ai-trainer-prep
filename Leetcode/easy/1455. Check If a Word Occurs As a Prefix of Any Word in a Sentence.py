# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description/

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # Time: O(n), n = len(sentence)
        # Space: O(n)
        sentence = sentence.split()
        length = len(searchWord)
        for i in range(len(sentence)):
            if sentence[i][:length] == searchWord:
                return i + 1
        return -1


