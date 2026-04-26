# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/circular-sentence/description/

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Time: O(n), n = len(sentence)
        # Space: O(n)
        words = sentence.split()
        prev = sentence[-1]
        for word in words:
            if prev[-1] != word[0]:
                return False
            prev = word
        return True


