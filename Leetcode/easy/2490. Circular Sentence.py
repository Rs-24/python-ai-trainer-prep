

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Time: O(n)
        # Space: O(n)
        s = sentence.split()
        p = s[-1]
        for w in s:
            if p[-1] != w[0]:
                return False
            p = w
        return True


