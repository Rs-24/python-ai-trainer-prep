# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/goat-latin/description/

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        # Time: O(n), n = len(sentence)
        # Space: O(n)
        sentence = sentence.split()
        for i, word in enumerate(sentence):
            if word[0].lower() in "aeiou":
                sentence[i] = word + "ma" + ("a" * (i + 1))
            else:
                sentence[i] = word[1:] + word[0] + "ma" + ("a" * (i + 1))       
        return " ".join(sentence)


