# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/number-of-valid-words-in-a-sentence/description/

class Solution:
    def countValidWords(self, sentence: str) -> int:
        # Time: O(n), n = len(sentence)
        # Space: O(n)
        count = 0
        for word in sentence.split():
            valid = True
            num_hyphens = 0
            length = len(word)
            for i, ch in enumerate(word):
                if ch.isdigit():
                    valid = False
                    break
                elif ch == "-":
                    num_hyphens += 1
                    if num_hyphens > 1 or i == 0 or i == length - 1 or not (word[i - 1].isalpha() and word[i + 1].isalpha()):
                        valid = False
                        break
                elif ch in "!.,":
                    if i != length - 1:
                        valid = False
                        break
            count += 1 if valid else 0
        return count


