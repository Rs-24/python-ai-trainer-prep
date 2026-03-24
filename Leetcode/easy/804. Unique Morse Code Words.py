# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/unique-morse-code-words/description/

from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Time: O(n), n = total number of characters in words
        # Space: O(n)
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                 "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
                 "..-","...-",".--","-..-","-.--","--.."]
        morse_words = []
        for word in words:
            temp = []
            for ch in word:
                temp.append(morse[ord(ch) - ord("a")])
            morse_words.append("".join(temp))
        return len(set(morse_words))


