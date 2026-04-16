# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/sorting-the-sentence/description/

class Solution:
    def sortSentence(self, s: str) -> str:
        # Time: O(1)
        # Space:(1)
        out = [""] * (s.count(" ") + 1)
        for word in s.split():
            out[int(word[-1]) - 1] = word[:-1]
        return " ".join(out)


