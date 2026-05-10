

class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        # Time: O(m * n), m = len(words), n = number of characters per word
        # in words
        # Space: O(m + n)
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                 "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
                 "..-","...-",".--","-..-","-.--","--.."]
        s = set()
        for word in words:
            s.add("".join(morse[ord(ch) - ord("a")] for ch in word))
        return len(s)


