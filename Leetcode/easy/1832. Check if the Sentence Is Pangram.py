

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Time: O(n), n = len(sentence)
        # Space: O(1)
        return len(set(sentence)) == 26


