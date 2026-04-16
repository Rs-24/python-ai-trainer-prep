# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Time: O(n), n = len(sentence)
        # Space: O(1)
        return len(set(sentence)) == 26


